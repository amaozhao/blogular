# coding: utf-8
'''
Created on 2015年1月9日

@author: amaozhao
'''

from blog.models import Comment
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from api.serializers.entry import CommentEntrySerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer(read_only=True)
    entry = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Comment
        depth = 1


class RecentCommentSerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer(read_only=True)
    entry = CommentEntrySerializer(read_only=True)

    class Meta:
        model = Comment
        depth = 1
