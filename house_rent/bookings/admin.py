from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'property', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('tenant__username', 'property__title')

admin.site.register(Booking, BookingAdmin)
