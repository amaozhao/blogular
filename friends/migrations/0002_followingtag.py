# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowingTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.ForeignKey(related_name='followingtags', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='tags', to='taggit.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
