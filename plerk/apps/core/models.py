from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db.models import UUIDField

from plerk.apps.core.managers import UserManager


class User(AbstractUser):
    """Custom User Model"""
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    objects = UserManager()
