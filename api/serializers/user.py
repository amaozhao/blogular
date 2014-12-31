# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')
