from django import forms

from Music_site_app_remake_exam.my_web.models import ProfileModel, AlbumModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username...'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email...'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age...'
                }
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            AlbumModel.objects.all().delete()
        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.required = False


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name...'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist...'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description...'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Link to Image...'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price...'
                }
            ),
        }

class AlbumCreateForm(AlbumBaseForm):
    pass
