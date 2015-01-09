# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friend',
                'verbose_name_plural': 'Friends',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
