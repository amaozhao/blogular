# coding: utf-8
'''
Created on 2015年1月9日

@author: amaozhao
'''
from friends.models import FriendShip, FollowingTag
from api.serializers.friendship import FriendshipSerializer, FollowingTagSerializer
from rest_framework import permissions
from api.permissions import FollowingOrReadOnly, ReadOnly, IsOwnerOrReadOnly
from rest_framework import viewsets


class FollowingViewSet(viewsets.ModelViewSet):
    model = FriendShip
    serializer_class = FriendshipSerializer
    permission_classes = (FollowingOrReadOnly, permissions.IsAuthenticatedOrReadOnly)
    paginate_by = 24
    
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)
        
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return FriendShip.objects.get_following(self.request.user)
        return []


class FollowedViewSet(viewsets.ModelViewSet):
    model = FriendShip
    serializer_class = FriendshipSerializer
    permission_classes = (ReadOnly, )
    paginate_by = 24
    
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return FriendShip.objects.get_followed(self.request.user)
        return []


class FollowingTagViewSet(viewsets.ModelViewSet):
    model = FollowingTag
    serializer_class = FollowingTagSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)
    paginate_by = 24
    
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return FollowingTag.objects.filter(author=self.request.user)
        return []
