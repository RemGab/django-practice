from typing import Any
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from store.models import Booking
from django.contrib.auth.decorators import login_required
from practice.forms import SignupForm, Blop
from django.views import View
from django.views.generic import TemplateView, ListView




class Bgview(ListView):
    model = Booking
    template_name = "account/index.html"
    context_object_name = 'article'



class HomeView(TemplateView):
    
    template_name = 'account/index.html'
    
    title = 'Default'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = self.title
        return context





def book(request):
    bookings = Booking.objects.all()
    return render(request,'index.html', {'bookings': bookings})

# @login_required
def books(request, slug):
    booking = get_object_or_404(Booking,slug=slug)
    return render(request,'book.html', context = {'booking': booking })


def signup(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci pour l'inscription")
    else :
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

def blop(request):
    if request.method == 'POST':
        form = Blop(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = Blop(initial={'title': 'titre temporaire'})
        
    return render(request, 'post.html', {'form':form})