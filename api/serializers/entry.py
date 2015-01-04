# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from blog.models import Entry
from rest_framework import serializers
from api.serializers.user import UserSerializer
from api.serializers.tag import TagSerializer


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Entry
        depth = 1
