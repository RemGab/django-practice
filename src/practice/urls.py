"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import book, books, signup, blop
from .views import HomeView, Bgview

urlpatterns = [
    path('',Bgview.as_view(), name='home'),
    path('about/',HomeView.as_view(title = 'abbouiututt'), name='about'),
    path('gestion-local/', admin.site.urls),
    path('signup/',signup, name='signup'),
    path('store/',book,name='store-index'),
    path('store/<str:slug>/', books,name='store-post'),
    path('article/', blop, name='blop'),
]
