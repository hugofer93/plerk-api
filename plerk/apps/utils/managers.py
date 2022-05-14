from django.db.models import Manager, QuerySet


class BaseQuerySet(QuerySet):
    """BaseQuerySet for BaseManager."""
    def all_active(self):
        return self.filter(is_active=True)


class BaseManager(Manager.from_queryset(BaseQuerySet)):
    """BaseManager for BaseModel."""
