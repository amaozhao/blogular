# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created', '-updated'], 'verbose_name': 'entry', 'verbose_name_plural': 'entries'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='excerpt',
            field=models.TextField(help_text='Used for search and SEO.', verbose_name='excerpt', editable=False, blank=True),
            preserve_default=True,
        ),
    ]
