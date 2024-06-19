from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from store.models import Booking

def book(request):
    bookings = Booking.objects.all()
    return render(request,'index.html', {'bookings': bookings})

def books(request, slug):
    booking = get_object_or_404(Booking,slug=slug)
    return render(request,'book.html', context = {'booking': booking })