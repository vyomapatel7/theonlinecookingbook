from django.shortcuts import render

profiles = [
    {
        'user': 'vyoma',
        'name': 'vyoma',
        'date_created': 'May 12, 2019'
    },
]

def profile_list(request):
    return render(request, 'book/profile_list.html', {})

def home(request):
    context = {
        'profiles': profiles
    }
    return render(request, 'book/home.html', context)

def about(request):
    return render(request, 'book/about.html', {})
