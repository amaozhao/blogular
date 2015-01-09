# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20150104_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date', db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated date', db_index=True)),
                ('author', models.ForeignKey(related_name='comments', verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('entry', models.ForeignKey(related_name='comments', verbose_name='entry', to='blog.Entry')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='comment',
            index_together=set([('created',)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.IntegerField(default=2, db_index=True, verbose_name='status', choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
