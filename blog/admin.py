# coding: utf-8
from django.forms import Media
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage

from blog.models import Entry, Comment


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """
    Mixin adding WYMeditor for editing Entry.content field.
    """

    def _media(self):
        """
        The medias needed to enhance the admin page.
        """
        def static_url(url):
            return staticfiles_storage.url('js/%s' % url)

        media = super(EntryAdmin, self).media

        media += Media(
            js=(
                static_url('libs/jquery/jquery.min.js'),
                static_url('admin.min.js'),
            ),
            css={'all': (
                '/static/css/codemirror.css',
                '/static/css/uikit.min.css',
                '/static/css/highlight/vs.css',
                '/static/css/uikit/htmleditor.min.css',
            )}
        )
        return media
    media = property(_media)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
