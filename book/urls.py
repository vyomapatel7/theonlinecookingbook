from django.urls import path
from . import views
from django.urls import path, include
from book.backends import MyRegistrationView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='book-home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/register/', MyRegistrationView.as_view(), 
    	name='registration_register'),
	path('accounts/create_profile/', views.create_profile, name='registration_create_profile'),
	path('profiles/<id>/edit/', views.edit_profile, name='edit_profile'),
	path('profiles/<id>/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
