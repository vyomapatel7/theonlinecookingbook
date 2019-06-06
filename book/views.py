from django.shortcuts import render, redirect
from book.forms import ProfileForm
from PIL import Image
from .models import Profile
from django.template.defaultfilters import slugify

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
    context = {
        'profile': profile
    }
    return render(request, 'book/profile.html', context)

def edit_profile(request, slug):
    # grab the object...
    profile = Profile.objects.get(slug=slug)
    # set the form we're using...
    form_class = ProfileForm
    if request.method == 'POST':
    # grab the data from the submitted form
        form = form_class(data=request.POST, instance=profile)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('profile_detail', slug=profile.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=profile)

    # and render the template
    return render(request, 'book/edit_profile.html', {
        'profile': profile,
        'form': form,
    })

def create_profile(request):
    form_class = ProfileForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
    # grab the data from the submitted form and apply to
    # the form
        form = form_class(request.POST)
        if profile.object.get(user=request.user).exists():
            return True
            profile = form.create()
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
        form = form_class()

    return render(request, 'book/create_profile.html', {
            'form': form,
    })


