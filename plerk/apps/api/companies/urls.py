from django.urls import path

from plerk.apps.api.companies.views import CompanyDetail, CompanySummary


app_name = 'companies'

urlpatterns = [
    path('summarize/', CompanySummary.as_view(), name='summarize'),
    path('<uuid:pk>/', CompanyDetail.as_view(), name='detail'),
]
