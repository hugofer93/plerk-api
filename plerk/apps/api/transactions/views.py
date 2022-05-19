from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import Response

from plerk.apps.api.transactions.serializers import \
    TransasctionSummarySerializer


class TransactionSummary(GenericAPIView):
    http_method_names = ['get', ]
    serializer_class = TransasctionSummarySerializer
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={})
        serializer.is_valid()
        return Response(serializer.data)
