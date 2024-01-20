from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'token', 'email_verify', 'is_active')
    list_filter = ('email_verify',)
    search_fields = ('email', 'last_name')
