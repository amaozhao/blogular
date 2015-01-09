# coding: utf-8
'''
Created on 2015年1月9日

@author: amaozhao
'''
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return False
