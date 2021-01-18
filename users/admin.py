from django.contrib import admin
# from django.contrib.admin import UserAdmin
from users.models import  Issue

# Register your models here.

# @admin.AdminSite(UserInfo)
# class UserInfoAdmin(UserAdmin):
#     list_display = ['username', 'is_superuser', 'last_login']

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_at', 'user_id']