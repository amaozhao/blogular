# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from taggit.models import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)
