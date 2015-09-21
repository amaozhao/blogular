# coding: utf-8

from api.serializers.archive import ArchiveSerializer
from rest_framework import generics
from blog.models import Entry


class ArchiveView(generics.ListAPIView):
    queryset = Entry.objects.datetimes('created', 'month', order='ASC')
    serializer_class = ArchiveSerializer
