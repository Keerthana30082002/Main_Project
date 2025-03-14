from django.urls import path
from .views import book_property, booking_list, approve_booking, reject_booking

urlpatterns = [
    path('book/<int:property_id>/', book_property, name='book_property'),
    path('list/', booking_list, name='booking_list'),
    path('approve/<int:booking_id>/', approve_booking, name='approve_booking'),
    path('reject/<int:booking_id>/', reject_booking, name='reject_booking'),
]
