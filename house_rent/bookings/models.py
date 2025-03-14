from django.db import models
from properties.models import Property
from users.models import CustomUser

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant.username} - {self.property.title} ({self.status})"
