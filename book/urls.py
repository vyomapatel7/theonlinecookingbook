from django.urls import path
from . import views
from django.urls import path, include
from book.backends import MyRegistrationView

urlpatterns = [
    path('', views.home, name='book-home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/register/', MyRegistrationView.as_view(),
	name='registration_register'),
	path('accounts/create_profile/', views.create_profile,
	name='registration_create_profile'),
	path('profiles/<slug>/edit/',
	views.edit_profile, name='edit_profile'),
	path('profiles/<id>/',
	views.profile, name='profile'),
]
