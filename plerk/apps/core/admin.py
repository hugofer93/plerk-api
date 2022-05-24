from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


UserModel = get_user_model()


# Custom AdminSite
class AdminSite(admin.AdminSite):
    admin.AdminSite.site_header = 'PLERK Admin'
    admin.AdminSite.site_title = admin.AdminSite.site_header


@admin.register(UserModel)
class UserAdmin(DjangoUserAdmin):
    """Custom User Admin for AdminSite"""
