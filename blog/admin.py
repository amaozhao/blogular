# coding: utf-8
from django.contrib import admin

from blog.models import Entry, Comment


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
