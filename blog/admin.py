from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'date_begin', 'activate')
    list_filter = ('date_begin', 'title', 'activate')
    search_fields = ('title', 'text')
