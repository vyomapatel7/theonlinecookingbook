from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='book-home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile')
]
