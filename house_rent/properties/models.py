from django.db import models
from users.models import CustomUser

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('rent', 'For Rent'),
        ('sale', 'For Sale'),
    )
    
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return self.title
