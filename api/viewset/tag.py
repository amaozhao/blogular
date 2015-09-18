# coding: utf-8
'''
Created on 2015年1月4日

@author: amaozhao
'''

from api.serializers.tag import TagSerializer
from api.serializers.entry import EntrySerializer
from api.permissions import ReadOnly, IsOwnerOrReadOnly
from taggit.models import Tag
from blog.models import Entry
from friends.models import FollowingTag
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class TagList(generics.ListAPIView):
    model = Tag
    queryset = Tag.objects.all()
    permission_classes = (ReadOnly,)
    serializer_class = TagSerializer
    paginate_by = 48


class FollowingTagList(viewsets.ModelViewSet):
    model = Tag
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = TagSerializer
    paginate_by = 48

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return FollowingTag.objects.get_or_create(
                author=self.request.user)[0].tags.all()
        return []

    def create(self, request, *args, **kwargs):
        tag_id = request.data.get('id', None)
        if tag_id:
            tag = Tag.objects.get(id=int(tag_id))
            followingtag = FollowingTag.objects.get_or_create(
                author=self.request.user)[0]
            followingtag.tags.add(tag)
            serializer = self.get_serializer(tag)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response()

    def destroy(self, request, *args, **kwargs):
        tag_id = kwargs.get('pk', None)
        if tag_id:
            tag = Tag.objects.get(id=int(tag_id))
            followingtag = FollowingTag.objects.get_or_create(
                author=self.request.user)[0]
            followingtag.tags.remove(tag)
            serializer = self.get_serializer(tag)
            return Response(serializer.data)
        return Response()


class TagDetail(generics.ListAPIView):
    model = Entry
    permission_classes = (ReadOnly,)
    serializer_class = EntrySerializer
    paginate_by = 20

    def get_queryset(self):
        tag_id = self.kwargs.get('id', None)
        if tag_id:
            tag = Tag.objects.get(id=int(tag_id))
            return Entry.objects.filter(tags__name__in=[tag.name, ]).distinct()
        return []
