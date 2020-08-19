from django.contrib import admin
from bookmark.models import Bookmark
from .models import Blog
# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')


# 참고 데코레이터를 사용안할 때 admin.site.register(Bookmark,BookmarkAdmin) 을 사용하기도 함

admin.site.register(Blog)