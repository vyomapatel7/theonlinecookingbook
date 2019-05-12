from django.shortcuts import render

def profile_list(request):
    return render(request, 'book/profile_list.html', {})
