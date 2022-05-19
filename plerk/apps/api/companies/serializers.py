from django.core.cache import cache
from rest_framework.serializers import (
    CharField,
    Serializer,
    SerializerMethodField,
    UUIDField,
)

from plerk.apps.companies.models import Company
from plerk.apps.transactions.models import Transaction


class CompanySerializer(Serializer):
    id = UUIDField(read_only=True)
    name = CharField(max_length=80, read_only=True)


def get_company_by_id_for_serializers(company_id):
    """Get company by id for serializers.

    Args:
        company_id (str): Company ID.

    Returns:
        dict, str: If company exists, company data serialized.
                else message "calculating".
    """
    if company_id:
        try:
            company = Company.objects.get_active_company(id=company_id)
        except Company.DoesNotExist:
            company = None

    if company_id and company:
        serializer = CompanySerializer(company)
        return serializer.data

    return 'calculating'


def get_company_id_from_cache(key):
    """Get company ID from cache.

    Args:
        key (str): Key in cache.

    Returns:
        dict, str: If company exists, company data serialized.
                else message "calculating".
    """
    company_id = cache.get(key, None)
    value = get_company_by_id_for_serializers(company_id)
    return value


class CompanySummarySerializer(Serializer):
    company_with_more_sales = SerializerMethodField()
    company_with_less_sales = SerializerMethodField()
    company_with_most_rejected_sales = SerializerMethodField()
    company_with_less_rejected_sales = SerializerMethodField()

    def get_company_with_more_sales(self, obj):
        value = get_company_id_from_cache('company_id_with_more_sales')
        return value

    def get_company_with_less_sales(self, obj):
        value = get_company_id_from_cache('company_id_with_less_sales')
        return value

    def get_company_with_most_rejected_sales(self, obj):
        value = get_company_id_from_cache(
            'company_id_with_most_rejected_sales')
        return value

    def get_company_with_less_rejected_sales(self, obj):
        value = get_company_id_from_cache(
            'company_id_with_less_rejected_sales')
        return value


class CompanyDetailSerializer(Serializer):
    name = CharField(max_length=80, read_only=True)
    number_successful_transactions = SerializerMethodField()
    number_rejected_transactions = SerializerMethodField()
    date_with_more_Transaccions = SerializerMethodField()

    def get_number_successful_transactions(self, obj):
        company_id = obj.id
        value = Transaction.objects.get_succes_transactions_company(
            company_id).count()
        return value

    def get_number_rejected_transactions(self, obj):
        company_id = obj.id
        value = Transaction.objects.get_rejected_transactions_company(
            company_id).count()
        return value

    def get_date_with_more_Transaccions(self, obj):
        company_id = obj.id
        value = Transaction.objects\
            .get_date_most_success_transactions_company(company_id)
        return value
