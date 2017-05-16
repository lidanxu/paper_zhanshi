# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhanshi', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AlterField(
            model_name='statistics',
            name='person_activity',
            field=models.ImageField(height_field=100, width_field=100, upload_to=b'media', blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='topic_activity',
            field=models.ImageField(height_field=100, width_field=100, upload_to=b'media', blank=True),
        ),
    ]
