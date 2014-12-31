# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from api.serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
