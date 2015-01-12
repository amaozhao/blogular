# coding: utf-8
'''
Created on 2015年1月4日

@author: amaozhao
'''

from api.serializers.tag import TagSerializer
from api.serializers.entry import EntrySerializer
from api.permissions import ReadOnly
from taggit.models import Tag
from blog.models import Entry
from rest_framework import generics


class TagList(generics.ListAPIView):
    model = Tag
    queryset = Tag.objects.all()
    permission_classes = (ReadOnly,)
    serializer_class = TagSerializer
    paginate_by = 48


class TagDetail(generics.ListAPIView):
    model = Entry
    permission_classes = (ReadOnly,)
    serializer_class = EntrySerializer
    paginate_by = 20
    
    def get_queryset(self):
        tag_id = self.kwargs.get('id', None)
        if tag_id:
            tag = Tag.objects.get(id=int(tag_id))
            return Entry.objects.filter(tags__name__in=[tag.name,]).distinct()
        return []
