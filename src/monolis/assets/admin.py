from django.contrib import admin
from .models import Asset

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_number', 'name', 'asset_type', 'manufacturer', 'status', 'purchase_date')
    list_filter = ('asset_type', 'status', 'manufacturer', 'purchase_date')
    search_fields = ('asset_number', 'name', 'model_number')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('asset_number',)
    
    fieldsets = (
        ('基本情報', {
            'fields': ('asset_number', 'name', 'asset_type', 'manufacturer', 'model_number')
        }),
        ('購入情報', {
            'fields': ('purchase_date', 'purchase_price')
        }),
        ('状態・場所', {
            'fields': ('status', 'location', 'notes')
        }),
        ('システム情報', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )