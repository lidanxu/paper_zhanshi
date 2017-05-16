# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhanshi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='potential',
            name='potentialtopic',
            field=models.ImageField(default=1, height_field=100, width_field=100, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='person_activity',
            field=models.ImageField(default=1, height_field=100, width_field=100, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='topic_activity',
            field=models.ImageField(default=1, height_field=100, width_field=100, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='answer1',
            field=models.IntegerField(default=0, verbose_name=b'question_answer_num=0'),
        ),
        migrations.AddField(
            model_name='topic',
            name='answer2',
            field=models.IntegerField(default=0, verbose_name=b'0<question_answer_num<99'),
        ),
        migrations.AddField(
            model_name='topic',
            name='answer3',
            field=models.IntegerField(default=0, verbose_name=b'100<=question_answer_num<500'),
        ),
        migrations.AddField(
            model_name='topic',
            name='answer4',
            field=models.IntegerField(default=0, verbose_name=b'500<=question_answer_num'),
        ),
    ]
