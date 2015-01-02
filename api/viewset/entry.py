# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from blog.models import Entry
from api.serializers.entry import EntrySerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.filter(status=2)
    serializer_class = EntrySerializer
    paginate_by = 20


class RecentEntryView(ListAPIView):
    model = Entry
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(status=2)[:5]


class FindViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.filter(status=2)
    serializer_class = EntrySerializer
    paginate_by = 20

    # def post(self, request, *args, **kwargs):
    #     return Response({}, status=403)
