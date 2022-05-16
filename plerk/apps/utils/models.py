from uuid import uuid4

from django.db.models import BooleanField, DateTimeField, Model, UUIDField

from plerk.apps.utils.managers import BaseManager


class BaseModel(Model):
    """Base Model for project."""
    is_active = BooleanField(default=True)
    creation_date = DateTimeField(auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ('-creation_date', )


class BaseUUIDModel(BaseModel):
    """Base UUID Model for project."""
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True
