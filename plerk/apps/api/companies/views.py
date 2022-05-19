from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from plerk.apps.api.companies.serializers import (
    CompanyDetailSerializer,
    CompanySummarySerializer,
)
from plerk.apps.companies.models import Company


class CompanySummary(GenericAPIView):
    http_method_names = ['get', ]
    serializer_class = CompanySummarySerializer
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={})
        serializer.is_valid()
        return Response(serializer.data)


class CompanyDetail(RetrieveAPIView):
    http_method_names = ['get', ]
    serializer_class = CompanyDetailSerializer
    permission_classes = [AllowAny, ]
    queryset = Company.objects.all_active()
