# coding: utf-8

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BlogConfig(AppConfig):

    """
    Config for blog application.
    """
    name = 'blog'
    label = 'blog'
    verbose_name = _('blog')
