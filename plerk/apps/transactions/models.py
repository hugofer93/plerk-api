from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    PROTECT,
)

from plerk.apps.companies.models import Company
from plerk.apps.transactions.managers import TransactionManager
from plerk.apps.utils.models import BaseUUIDModel


class Transaction(BaseUUIDModel):
    TAX_PERCENTAGE = Decimal('0.12')

    CLOSED_STATUS = 'closed'
    REVERSED_STATUS = 'reversed'
    PENDING_STATUS = 'pending'
    STATUS_CHOICES = (
        (CLOSED_STATUS, 'closed'),
        (REVERSED_STATUS, 'reversed'),
        (PENDING_STATUS, 'pending'),
    )

    company = ForeignKey(Company, on_delete=PROTECT)
    price = DecimalField(max_digits=10, decimal_places=2)
    date = DateTimeField()
    status = CharField(max_length=10, choices=STATUS_CHOICES)
    status_approved = BooleanField()
    final_payment = BooleanField()
    tax_value = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00')), ],
    )

    objects = TransactionManager()

    @property
    def subtotal(self):
        """Calculate the subtotal. (Subtracts the tax from the price)

        Returns:
            Decimal: Subtotal.
        """
        tax = self.tax_value or Decimal('0.00')
        price = self.price or Decimal('0.00')
        subtotal = price - tax
        if subtotal < Decimal('0.00'): subtotal = Decimal('0.00')
        return subtotal

    @classmethod
    def calculate_tax(cls, value=Decimal('0.00'), has_tax_included=True):
        """Calculate the tax of a transaction.

        Args:
            value (Decimal): Base value to calculate the tax.
            has_tax_included (bool, optional):
                Indicate if the price includes tax. Defaults to True.

        Returns:
            Decimal: Transaction tax.
        """
        if not value >= Decimal('0.01'):
            tax = Decimal('0.00')
            return tax

        if has_tax_included:
            subtotal = round(value / (1+cls.TAX_PERCENTAGE), ndigits=2)
            tax = value - subtotal
        else:
            tax = round(value * cls.TAX_PERCENTAGE, ndigits=2)
        return tax

    def __str__(self) -> str:
        return f'Price: {self.price} | Status: {self.status}'
