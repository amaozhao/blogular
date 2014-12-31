# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('excerpt', models.TextField(help_text='Used for search and SEO.', verbose_name='excerpt', blank=True)),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('status', models.IntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date', db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated date', db_index=True)),
                ('author', models.ForeignKey(related_name='entries', verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'entry',
                'verbose_name_plural': 'entries',
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='entry',
            index_together=set([('created',), ('status', 'created')]),
        ),
    ]
