# coding: utf-8
'''
Created on 2015年1月9日

@author: amaozhao
'''
from friends.models import FriendShip
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class FriendshipSerializer(serializers.ModelSerializer):
    to_user = UserDetailsSerializer()
    from_user = UserDetailsSerializer()

    class Meta:
        model = FriendShip
        fields = ('id', 'from_user', 'to_user',)
        depth = 1
