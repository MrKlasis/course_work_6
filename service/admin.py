from django.contrib import admin

from service.models import Client, Massage, Mailing, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'author')
    list_filter = ('author',)
    search_fields = ('email', 'name', 'author')


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'massage', 'periodic', 'status', 'author', 'is_active')
    list_filter = ('is_active', 'periodic', 'status')
    search_fields = ('name', 'author')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'time_attempt', 'status', 'mode', 'mail_server_response')
    list_filter = ('status', 'mode')
    search_fields = ('name',)
