# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhanshi', '0002_auto_20170511_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'/home/linda/Practices/examples/django/zhanshisite/media', blank=True)),
                ('externalURL', models.URLField(blank=True)),
            ],
        ),
    ]
