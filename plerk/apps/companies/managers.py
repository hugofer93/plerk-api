from django.db.models import Count, Manager

from plerk.apps.utils.managers import BaseQuerySet


class CompanyQuerySet(BaseQuerySet):
    def get_active_company(self, id):
        """Get active company by ID.

        Args:
            id (UUID): Company ID.

        Returns:
            Model: Company instance.
        """
        company = self.all_active().get(id=id)
        return company

    def get_companies_by_num_success_transactions(self, asc_order=True):
        """Get companies by number of successful transactions.

        Args:
            asc_order (bool, optional): Ascending order.
                                        Defaults to True.

        Returns:
            QuerySet: Companies list
        """
        attr = 'num_transactions'
        if not asc_order: attr = f'-{attr}'
        companies = self.annotate(num_transactions=Count('transaction'))\
            .all_active().filter(
                transaction__is_active=True,
                transaction__final_payment=True).order_by(attr)
        return companies

    def get_company_with_more_sales(self):
        """Get company with more sales.

        Returns:
            Model: Company instance.
        """
        company = self.get_companies_by_num_success_transactions(
            asc_order=False).first()
        return company

    def get_company_with_less_sales(self):
        """Get company with less sales.

        Returns:
            Model: Company instance.
        """
        company = self.get_companies_by_num_success_transactions()\
            .first()
        return company

    def get_companies_by_num_rejected_sales(self, asc_order=True):
        """Get companies by number of rejected sales.

        Args:
            asc_order (bool, optional): Ascending order.
                                        Defaults to True.

        Returns:
            QuerySet: Companies list
        """
        attr = 'num_sales'
        if not asc_order: attr = f'-{attr}'
        companies = self.annotate(num_sales=Count('transaction'))\
            .all_active().filter(
                transaction__is_active=True,
                transaction__final_payment=False).order_by(attr)
        return companies

    def get_company_with_most_rejected_sales(self):
        """Get company with most rejected sales.

        Returns:
            Model: Company instance.
        """
        company = self.get_companies_by_num_rejected_sales(asc_order=False)\
            .first()
        return company

    def get_company_with_less_rejected_sales(self):
        """Get company with less rejected sales.

        Returns:
            Model: Company instance.
        """
        company = self.get_companies_by_num_rejected_sales().first()
        return company


class CompanyManager(Manager.from_queryset(CompanyQuerySet)):
    """Custom Manager for Company Model."""
