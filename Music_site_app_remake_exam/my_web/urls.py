from django.urls import path, include

from Music_site_app_remake_exam.my_web.views import index, profile_details, profile_delete, album_add, album_details, \
    album_edit, album_delete, profile_create

urlpatterns = (
    path('', index, name='index'),

    path('profile/', include([
        path('details/', profile_details, name='profile-details'),
        path('delete/', profile_delete, name='profile-delete'),
        path('create/', profile_create, name='profile-create'),
    ])),

    path('album/', include([
        path('add/', album_add, name='album-add'),
        path('details/<int:pk>/', album_details, name='album-details'),
        path('edit/<int:pk>/', album_edit, name='album-edit'),
        path('delete/<int:pk>/', album_delete, name='album-delete'),
    ]))
)

"""
http://localhost:8000/ - home page

http://localhost:8000/album/add/ - add album page
http://localhost:8000/album/details/<id>/ - album details page
http://localhost:8000/album/edit/<id>/ - edit album page
http://localhost:8000/album/delete/<id>/ - delete album page

http://localhost:8000/profile/details/ - profile details page
http://localhost:8000/profile/delete/ - delete profile page
"""
