from django.urls import path

from plerk.apps.api.transactions.views import TransactionSummary


app_name = 'transactions'

urlpatterns = [
    path('summarize/', TransactionSummary.as_view(), name='summarize'),
]
