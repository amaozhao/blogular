# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_followingtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followingtag',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='taggit.Tag', blank=True),
        ),
    ]
