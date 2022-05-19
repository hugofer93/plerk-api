from django.db.models import Count, Manager, Sum
from django.db.models.functions import TruncDate

from plerk.apps.utils.managers import BaseQuerySet


class TransactionQuerySet(BaseQuerySet):
    def get_successful_transactions(self):
        """get successfull transactions.

        Returns:
            QuerySet: Transaction list.
        """
        transactions = self.all_active().filter(final_payment=True)
        return transactions

    def get_sum_price_success_transactions(self):
        """Get sum of prices of successful transactions.

        Returns:
            Decimal: Total price.
        """
        total_price = self.get_successful_transactions()\
            .aggregate(total_price=Sum('price')).get('total_price')
        return total_price

    def get_rejected_transactions(self):
        """Get rejected transactions.

        Returns:
            QuerySet: Transaction list.
        """
        transactions = self.all_active().filter(final_payment=False)
        return transactions

    def get_sum_price_rejected_transactions(self):
        """Get sum of prices of rejected transactions.

        Returns:
            Decimal: Total price.
        """
        total_price = self.get_rejected_transactions()\
            .aggregate(total_price=Sum('price')).get('total_price')
        return total_price

    def get_succes_transactions_company(self, company_id):
        """Get all successful transactinos of a company.

        Args:
            company_id (UUID): Company ID.

        Returns:
            QuerySet: Transaction list.
        """
        transactions = self.select_related('company')\
            .get_successful_transactions()\
            .filter(company_id=company_id)
        return transactions

    def get_rejected_transactions_company(self, company_id):
        """Get all rejected transactinos of a company.

        Args:
            company_id (UUID): Company ID.

        Returns:
            QuerySet: Transaction list.
        """
        transactions = self.select_related('company')\
            .get_rejected_transactions()\
            .filter(company_id=company_id)
        return transactions

    def get_date_most_success_transactions_company(self, company_id):
        """Get date with most successful transactions of the company.

        Args:
            company_id (UUID): Company ID.

        Returns:
            str: Only date without time.
        """
        date = self.get_succes_transactions_company(company_id)\
            .values('date').annotate(trunc_date=TruncDate('date'))\
            .values('trunc_date').annotate(count_date=Count('trunc_date'))\
            .order_by('-count_date').first().get('trunc_date')
        return date

class TransactionManager(Manager.from_queryset(TransactionQuerySet)):
    """"Transaction Manager."""
