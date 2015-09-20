# coding: utf-8

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TaggitConfig(AppConfig):

    """
    Config for taggit application.
    """
    name = 'taggit'
    label = 'taggit'
    verbose_name = _('taggit')
