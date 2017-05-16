#-*- coding:utf-8 -*-
from django.contrib import admin
from .models import *
admin.site.register(Topic)
admin.site.register(Potential)
admin.site.register(Statistics)
from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ( 'image_tag','title','description','image','externalURL', )
    readonly_fields = ('image_tag',)

admin.site.register(Image, ImageAdmin)

class PhotoAdmin(admin.ModelAdmin):
    # 將 image_tag 函示加入成為其中一個欄位

    readonly_fields = ('image_tag',)
    # (optional)若無此行，則會多出一個欄位顯示 image 的 url 與上傳圖片按鈕，如果希望從後台可以修改圖片，可將此行刪除

    exclude = ('image_file',)

admin.site.register(Photo, PhotoAdmin)
