# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from taggit.managers import TaggableManager

from markdown import markdown

DRAFT = 0
HIDDEN = 1
PUBLISHED = 2
STATUS_CHOICES = (
    (DRAFT, _('draft')),
    (HIDDEN, _('hidden')),
    (PUBLISHED, _('published'))
)


@python_2_unicode_compatible
class Entry(models.Model):
    author = models.ForeignKey(
        User,
        related_name='entries',
        verbose_name=_('author')
    )
    title = models.CharField(_('title'), max_length=255)
    content = models.TextField(_('content'), blank=True)
    excerpt = models.TextField(
        _('excerpt'),
        blank=True,
        help_text=_('Used for search and SEO.')
    )
    featured = models.BooleanField(_('featured'), default=False)
    status = models.IntegerField(
        _('status'),
        db_index=True,
        choices=STATUS_CHOICES,
        default=DRAFT
    )
    tags = TaggableManager()
    created = models.DateTimeField(
        _('created date'),
        db_index=True,
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _('updated date'),
        db_index=True,
        auto_now=True
    )

    @property
    def html(self):
        return markdown(self.content, ['markdown.extensions.fenced_code'])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name = _('entry')
        verbose_name_plural = _('entries')
        index_together = [
            ['created', ],
            ['status', 'created']
        ]
