from django.core.cache import cache
from rest_framework.serializers import (
    Serializer,
    SerializerMethodField,
)


class TransasctionSummarySerializer(Serializer):
    total_price_successful_transactions = SerializerMethodField()
    total_price_rejected_transactions = SerializerMethodField()

    def get_total_price_successful_transactions(self, obj):
        value = cache.get('sum_price_success_transactions', None)
        if not value: value = 'calculating'
        return value

    def get_total_price_rejected_transactions(self, obj):
        value = cache.get('sum_price_rejected_transactions', None)
        if not value: value = 'calculating'
        return value
