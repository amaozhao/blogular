# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from blog.models import Entry
from rest_framework import serializers
from api.serializers.user import UserSerializer
from api.serializers.tag import BaseTagSerializer


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = BaseTagSerializer(many=True, read_only=True)

    def create(self, validated_data):
        instance = super(EntrySerializer, self).create(validated_data)
        tags = self._context['request'].data['tags']
        instance.tags.add(*tags)
        return instance

    def update(self, instance, validated_data):
        instance = super(EntrySerializer, self).update(
            instance, validated_data)
        tags = self._context['request'].data['tags']
        instance.tags.set(*tags)
        return instance

    class Meta:
        model = Entry
        depth = 1
