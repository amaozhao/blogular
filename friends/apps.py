# coding: utf-8

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FriendConfig(AppConfig):

    """
    Config for friend application.
    """
    name = 'friend'
    label = 'friend'
    verbose_name = _('friend')
