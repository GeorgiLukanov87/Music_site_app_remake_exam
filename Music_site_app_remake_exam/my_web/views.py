from django.shortcuts import render, redirect


def index(request):
    profile = None
    if profile is None:
        return redirect('profile-create')

    return render(request, 'index.html')


def profile_create(request):
    return render(request, 'profile/profile-create.html')


def profile_details(request):
    return render(request, '/')


def profile_delete(request):
    return render(request, '/')


def album_add(request):
    return render(request, '/')


def album_details(request):
    return render(request, '/')


def album_edit(request):
    return render(request, '/')


def album_delete(request):
    return render(request, '/')
