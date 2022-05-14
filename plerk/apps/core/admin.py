from django.contrib.admin import register as admin_resgiter
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


UserModel = get_user_model()


@admin_resgiter(UserModel)
class UserAdmin(DjangoUserAdmin):
    """Custom User Admin for AdminSite"""
