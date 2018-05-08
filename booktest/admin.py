from django.contrib import admin

# Register your models here.
from .models import *

#第一种方式
class BookInfoAdmin(admin.ModelAdmin):

    list_display = ['id','btitle','bpub_date']


admin.site.register(BookInfo,BookInfoAdmin)

#第二种方式
#admin.site.register(HeroInfo,)
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hcontent']


