from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Music_site_app_remake_exam.my_web.urls')),
]
