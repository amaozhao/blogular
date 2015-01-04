# coding: utf-8
from django.contrib import admin

from blog.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass
