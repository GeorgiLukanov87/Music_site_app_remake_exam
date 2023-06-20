from django.shortcuts import render, redirect

from Music_site_app_remake_exam.my_web.models import ProfileModel


def get_profile():
    return ProfileModel.objects.first()


def index(request):
    profile = get_profile()

    if profile is None:
        return redirect('profile-create')

    return render(request, 'index.html')


def profile_create(request):
    return render(request, 'profile/profile-create.html')


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')


def album_add(request):
    return render(request, 'album/add-album.html')


def album_details(request, pk):
    return render(request, 'album/album-details.html')


def album_edit(request, pk):
    return render(request, 'album/edit-album.html')


def album_delete(request, pk):
    return render(request, 'album/delete-album.html')
