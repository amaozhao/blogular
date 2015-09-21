# coding: utf-8

from rest_framework import serializers


class ArchiveSerializer(serializers.Serializer):
    year = serializers.CharField(max_length=4)
    month = serializers.CharField(max_length=2)
