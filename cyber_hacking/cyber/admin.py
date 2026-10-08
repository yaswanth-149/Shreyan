from django.contrib import admin
from .models import CyberBreachData

# Register your models here.

@admin.register(CyberBreachData)
class CyberBreachDataAdmin(admin.ModelAdmin):
    # Columns displayed in admin table list view
    list_display = ('entity', 'year', 'records', 'org_type', 'methods', 'created_at')
    
    # Enable search by entity or methods
    search_fields = ('entity', 'org_type', 'methods')
    
    # Enable quick filter by year
    list_filter = ('year', 'org_type')