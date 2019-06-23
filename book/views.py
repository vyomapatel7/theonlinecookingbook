from django.shortcuts import render, redirect
from book.forms import ProfileForm
from book.forms import BookForm
from PIL import Image
from .models import Profile
from django.template.defaultfilters import slugify
from .models import Book

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
        'profiles': profile
    }
    return render(request, 'book/about.html', context)

def profile(request, id):
    profile = Profile.objects.get(id=id)
    books = Book.objects.filter(user=profile.user)
    context = {
        'profile': profile,
        'books': books
    }
    return render(request, 'book/profile.html', context)

def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    form_class = ProfileForm
    if request.method == 'POST':
    # grab the data from the submitted form
        form = form_class(request.POST, instance=profile)
        if Profile.objects.filter(user=request.user).exists():
                if form.is_valid():
                    profile = form.save(commit=False)
                    profile.user = request.user
                    profile.save()
                    return redirect('home')

    # otherwise just create the form
    else:
        form = form_class(instance=profile)

    return render(request, 'book/edit_profile.html', {
        'profile': profile,
        'form': form,
    })

def create_profile(request):
    profile = None
    if Profile.objects.filter(user=request.user).exists():
        profile = Profile.objects.get(user=request.user)
    form_class = ProfileForm
    if request.method == 'POST':
        form = form_class(request.POST, instance=profile)
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.get(user=request.user)
            return redirect(reverse('edit_profile', kwargs={'id': profile.id }))
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    # grab the data from the submitted form and apply to
    # the form
        form = form_class(request.POST)
        if Profile.objects.get(user=request.user):
            if form.is_valid():
            # create an instance but do not save yet
                profile = form.save(commit=False)
                # set the additional details
                profile.user = request.user
                # save the object
                profile.save()
                # redirect to our newly created thing
                return redirect('profile_detail')
                # otherwise just create the form
    else:
        form = form_class(instance=profile)

    return render(request, 'book/create_profile.html', {
        'form': form,
        'profile': profile,
    })

def create_book(request):
    form_class = BookForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('profile')

    else:      
        form = form_class()

    return render(request, 'book/create_book.html', {
        'form': form,
    })
