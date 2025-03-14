from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'location', 'price', 'property_type', 'is_available')
    list_filter = ('property_type', 'is_available')
    search_fields = ('title', 'location', 'owner__username')

admin.site.register(Property, PropertyAdmin)
