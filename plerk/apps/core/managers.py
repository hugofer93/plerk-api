from django.contrib.auth.models import UserManager as DjangoUserManager


class UserManager(DjangoUserManager):
    """Custom manager for User Model."""

    def all_active(self):
        return self.filter(is_active=True)
