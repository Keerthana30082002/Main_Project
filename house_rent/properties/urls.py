from django.urls import path
from .views import property_list, property_detail, add_property

urlpatterns = [
    path('', property_list, name='property_list'),
    path('<int:property_id>/', property_detail, name='property_detail'),
    path('add/', add_property, name='add_property'),
]
