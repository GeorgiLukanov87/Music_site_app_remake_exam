from django.contrib import admin

from Music_site_app_remake_exam.my_web.models import ProfileModel, AlbumModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'age', 'email',)


@admin.register(AlbumModel)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_name', 'artist', 'genre', 'price',)
