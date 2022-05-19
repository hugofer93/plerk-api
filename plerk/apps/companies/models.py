from django.db.models import CharField

from plerk.apps.companies.managers import CompanyManager
from plerk.apps.utils.models import BaseUUIDModel


class Company(BaseUUIDModel):
    name = CharField(max_length=80)

    objects = CompanyManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
