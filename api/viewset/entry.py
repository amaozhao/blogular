# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from blog.models import Entry
from taggit.models import Tag
from api.serializers.tag import TagSerializer
from api.serializers.entry import EntrySerializer
from api.permissions import IsOwnerOrReadOnly, ReadOnly
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.filter(status=2)
    serializer_class = EntrySerializer
    permission_classes = (IsOwnerOrReadOnly,)
    paginate_by = 10

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecentEntryView(ListAPIView):
    model = Entry
    serializer_class = EntrySerializer
    permission_classes = (ReadOnly,)

    def get_queryset(self):
        return Entry.objects.filter(status=2)[:5]

    def post(self, request, *args, **kwargs):
        return Response({}, status=403)


class ArchiveEntryView(ListAPIView):
    queryset = Entry.objects.filter(status=2)
    model = Entry
    serializer_class = EntrySerializer
    permission_classes = (ReadOnly,)
    paginate_by = 20

    def get_queryset(self):
        queryset = super(ArchiveEntryView, self).get_queryset()
        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        if year and month:
            return queryset.filter(created__year=year, created__month=month)
        return queryset

    def post(self, request, *args, **kwargs):
        return Response({}, status=403)


class UserEntryView(ListAPIView):
    model = Entry
    serializer_class = EntrySerializer
    permission_classes = (ReadOnly, )
    paginate_by = 20

    def get_queryset(self):
        user_id = int(self.kwargs['id'])
        return Entry.objects.filter(status=2, author=user_id)

    def post(self, request, *args, **kwargs):
        return Response({}, status=403)


class FindViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (ReadOnly,)
    paginate_by = 24

    def post(self, request, *args, **kwargs):
        return Response({}, status=403)
