from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='book-home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('registration.backends.simple.urls')),
]
