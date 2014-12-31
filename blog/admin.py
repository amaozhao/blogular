# coding: utf-8
from django.contrib import admin

from django.utils.html import strip_tags
from django.utils.text import Truncator

from blog.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
     # Custom Methods
    def save_model(self, request, entry, form, change):
        """
        Save the authors, update time, make an excerpt.
        """
        entry.excerpt = Truncator(strip_tags(entry.html)).words(50)
        entry.save()
