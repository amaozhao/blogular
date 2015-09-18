# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from taggit.models import Tag
from rest_framework import serializers
from friends.models import FollowingTag


class BaseTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name',)


class TagSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(TagSerializer, self).to_representation(instance)
        user = self._context['request'].user
        if user.is_authenticated() and FollowingTag.objects.filter(
                author=user, tags=instance).exists():
            ret['added'] = True
        else:
            ret['added'] = False
        return ret

    class Meta:
        model = Tag
        fields = ('id', 'name',)
