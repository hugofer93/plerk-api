from django.contrib import admin

from plerk.apps.transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company', 'price', 'subtotal', 'tax_value', 'date', 'status',
        'status_approved', 'final_payment', 'creation_date', 'is_active'
    )
    list_display_links = ('id', 'company')
    search_fields = ('company__name', 'status')
    list_filter = (
        'company__name', 'date', 'status',
        'status_approved', 'final_payment'
    )
    readonly_fields = (
        'id', 'company', 'price', 'subtotal', 'tax_value', 'date',
        'status', 'status_approved','final_payment', 'is_active'
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
