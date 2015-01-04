# coding: utf-8
'''
Created on 2015年1月4日

@author: amaozhao
'''


from api.serializers.tag import TagSerializer
from taggit.models import Tag
from rest_framework import viewsets


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
