# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', verbose_name=_('profile'))
