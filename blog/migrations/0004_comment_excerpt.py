# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150109_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='excerpt',
            field=models.TextField(verbose_name='excerpt', editable=False, blank=True),
        ),
    ]
