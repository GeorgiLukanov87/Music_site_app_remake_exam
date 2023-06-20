from django.shortcuts import render, redirect

from Music_site_app_remake_exam.my_web.forms import ProfileCreateForm, ProfileDeleteForm, AlbumCreateForm
from Music_site_app_remake_exam.my_web.models import ProfileModel, AlbumModel


def get_profile():
    return ProfileModel.objects.first()


def index(request):
    profile = get_profile()
    albums = AlbumModel.objects.all()

    if profile is None:
        return redirect('profile-create')

    context = {'profile': profile, 'albums': albums, }

    return render(request, 'index.html', context, )


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }

    return render(request, 'profile/profile-create.html', context, )


def profile_details(request):
    profile = get_profile()
    albums = AlbumModel.objects.all()
    context = {'profile': profile, 'albums': albums, }
    return render(request, 'profile/profile-details.html', context, )


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }
    return render(request, 'profile/profile-delete.html', context, )


def album_add(request):
    profile = get_profile()

    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }
    return render(request, 'album/add-album.html', context, )


def album_details(request, pk):
    return render(request, 'album/album-details.html')


def album_edit(request, pk):
    return render(request, 'album/edit-album.html')


def album_delete(request, pk):
    return render(request, 'album/delete-album.html')
