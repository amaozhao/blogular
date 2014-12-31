# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

"""Apps for blog"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BlogConfig(AppConfig):
    """
    Config for blog application.
    """
    name = 'blog'
    label = 'blog'
    verbose_name = _('blog')
