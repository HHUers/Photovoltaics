from django.contrib import admin

from apps.users.models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ['nick_name', 'gender', 'birthday']
    search_fields = ['nick_name']
    list_filter = ['gender']


admin.site.register(UserProfile, UserAdmin)
