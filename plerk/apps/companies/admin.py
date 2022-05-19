from django.contrib import admin

from plerk.apps.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creation_date', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('creation_date', 'is_active')
    readonly_fields = ('id', 'name', 'creation_date', 'is_active')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
