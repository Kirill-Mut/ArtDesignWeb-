from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Application
from .models import House, ExteriorPhoto, InteriorPhoto, Room
from .models import Contacts

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegistrationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user = authenticate(username=user.username, password=self.cleaned_data['password1'])
            login(self.request, user)
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))










class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone', 'email', 'message']
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'email': 'Электронная почта',
            'message': 'Сообщение',
        }


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['platform', 'url']




class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'model_3d', 'description', 'total_area', 'effective_area', 
                  'price', 'blueprint']

class ExteriorPhotoForm(forms.ModelForm):
    class Meta:
        model = ExteriorPhoto
        fields = ['photo']

class InteriorPhotoForm(forms.ModelForm):
    class Meta:
        model = InteriorPhoto
        fields = ['photo']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'area']
        
class RoomFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = True

RoomFormSet = forms.inlineformset_factory(
    House, Room, form=RoomForm, formset=RoomFormSet, extra=0, can_delete=False
)

ExteriorPhotoFormSet = forms.inlineformset_factory(
    House, ExteriorPhoto, form=ExteriorPhotoForm, extra=0, can_delete=False
)

InteriorPhotoFormSet = forms.inlineformset_factory(
    House, InteriorPhoto, form=InteriorPhotoForm, extra=0, can_delete=False
)