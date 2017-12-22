from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)