from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # App URLs
    path('users/', include('users.urls')),          # User Authentication URLs
    path('properties/', include('properties.urls')),  # Property Management URLs
    path('bookings/', include('bookings.urls')),    # Booking System URLs
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
