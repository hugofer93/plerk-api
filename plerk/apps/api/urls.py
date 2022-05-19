from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from plerk.apps.api.companies import urls as companies_urls
from plerk.apps.api.transactions import urls as transactions_urls


app_name = 'api'

urlpatterns = [
    path(
        'companies/',
        include(companies_urls, namespace='companies')
    ),
    path(
        'transactions/',
        include(transactions_urls, namespace='transactions')
    ),
]

docs_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]

urlpatterns += docs_urlpatterns
