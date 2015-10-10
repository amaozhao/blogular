# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from blog.models import Entry
from rest_framework import serializers
from api.serializers.tag import BaseTagSerializer
from rest_auth.serializers import UserDetailsSerializer


class EntrySerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer(read_only=True)
    tags = BaseTagSerializer(many=True, read_only=True)
    url = serializers.URLField(max_length=100, read_only=True)

    def create(self, validated_data):
        instance = super(EntrySerializer, self).create(validated_data)
        tags = self._context['request'].data.get('tags', [])
        if tags:
            instance.tags.add(*tags)
        return instance

    def update(self, instance, validated_data):
        instance = super(EntrySerializer, self).update(
            instance, validated_data)
        tags = self._context['request'].data.get('tags', [])
        instance.tags.set(*tags)
        return instance

    class Meta:
        model = Entry
        depth = 1


class CommentEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        depth = 1
        fields = ['id', 'title', ]
