from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    PROTECT,
)

from plerk.apps.companies.models import Company
from plerk.apps.utils.models import BaseUUIDModel


class Transaction(BaseUUIDModel):
    CLOSED_STATUS = 'closed'
    REVERSED_STATUS = 'reversed'
    PENDING_STATUS = 'pending'
    STATUS_CHOICES = (
        (CLOSED_STATUS, 'closed'),
        (REVERSED_STATUS, 'reversed'),
        (PENDING_STATUS, 'pending'),
    )

    company = ForeignKey(Company, on_delete=PROTECT)
    price = DecimalField(max_digits=8, decimal_places=2)
    date = DateTimeField()
    status = CharField(max_length=10, choices=STATUS_CHOICES)
    approval_status = BooleanField()
    final_payment = BooleanField()

    def __str__(self) -> str:
        return f'Price: {self.price} | Status: {self.status}'
