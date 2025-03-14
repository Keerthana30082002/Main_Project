from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from properties.models import Property
from django.contrib.auth.decorators import login_required

@login_required
def book_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    
    # Ensure only tenants can book properties
    if request.user.user_type != "tenant":
        return redirect('property_list')

    if request.method == "POST":
        Booking.objects.create(tenant=request.user, property=property_obj)
        return redirect('booking_list')

    return render(request, 'bookings/book_property.html', {'property': property_obj})

@login_required
def booking_list(request):
    if request.user.user_type == 'owner':
        bookings = Booking.objects.filter(property__owner=request.user)
    else:
        bookings = Booking.objects.filter(tenant=request.user)
        
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.property.owner == request.user:
        booking.status = "approved"
        booking.save()
    return redirect('booking_list')

@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.property.owner == request.user:
        booking.status = "rejected"
        booking.save()
    return redirect('booking_list')
