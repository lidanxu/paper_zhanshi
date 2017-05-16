#-*- coding:utf8 -*-
'''
topic,数据特点，话题活跃度，用户活跃度，主题分布
'''
from django.db import models

class Topic(models.Model):
    '''
    数据集大小，特点（问题分布）
    一张图（柱状图）
    '''
    corpus_number = models.IntegerField(default=0)   #采集的数据集大小
    question_num = models.IntegerField(default=0)     #采集的问题数量
    answer_num = models.IntegerField(default=0)   #采集的回答数是多少
    answer1=models.IntegerField('question_answer_num=0',default=0)
    answer2 = models.IntegerField('0<question_answer_num<99',default=0)
    answer3 = models.IntegerField('100<=question_answer_num<500',default=0)
    answer4 = models.IntegerField('500<=question_answer_num',default=0)

class Statistics(models.Model):
    '''
    话题活跃度+ 用户活跃度
    （两张图）
    '''
    topic_activity = models.ImageField(upload_to='media',height_field=100,width_field=100,blank=True)
    person_activity = models.ImageField(upload_to='media',height_field=100,width_field=100,blank=True)

   # def image_tag(self):
   #     return u'<img src="%s" />' % ''
   # image_tag.short_description = 'Image'
   # image_tag.allow_tags = True

class Potential(models.Model):
    '''
    柱状图表示主题分布情况
    最大概率的两个主题对应的词分布（折线图\柱状图？）
    '''
    potentialtopic = models.ImageField(height_field=100,width_field=100)

import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
class Image(models.Model):
   # allows for an image to be either stored in the MEDIA_ROOT path or
   # be a reference to an external URL to an image.
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    externalURL = models.URLField(blank=True)

    def url(self):
        # returns a URL for either internal stored or external image url
        if self.externalURL:
            return self.externalURL
        else:
            # is this the best way to do this??
            return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.image)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()) )
    image_tag.short_description = 'Image'    

    def __unicode__(self):
        # add __str__() if using Python 3.x
        return self.title
from django.utils.translation import ugettext_lazy as _

class Photo(models.Model):
    image = models.ImageField()
  
    # 用 html 語法嵌入 Admin 頁面

    def image_tag(self):
        return u'<img src="%s" width="200px" />' % self.img_file.url  
    # 欄位名稱

    image_tag.short_description = _('image')
    # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字

    image_tag.allow_tags = True
