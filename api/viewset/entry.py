# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from blog.models import Entry
from api.serializers.entry import EntrySerializer
from rest_framework import viewsets


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.filter(status=2)
    serializer_class = EntrySerializer
    paginate_by = 20
