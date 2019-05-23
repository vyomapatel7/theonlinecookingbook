from django.shortcuts import render
from PIL import Image
from .models import Profile

profiles = [
    {
        'user': 'vyoma',
        'name': 'vyoma',
        'date_created': 'May 12, 2019',
        'picture': 'image',
        'bio': 'bio'
    },
]

def profile_list(request):
    return render(request, 'book/profile_list.html', {})

def home(request):
    profile = Profile.objects.all()
    context = {
        'profiles': profile
    }
    return render(request, 'book/home.html', context)

def about(request):
    context = {
        'profiles': profiles
    }
    return render(request, 'book/about.html', context)

def profile(request):
    profile = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'book/profile.html', context)
