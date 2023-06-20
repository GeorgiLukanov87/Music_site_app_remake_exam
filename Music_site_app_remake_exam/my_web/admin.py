from django.contrib import admin

from Music_site_app_remake_exam.my_web.models import ProfileModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'age', 'email',)
