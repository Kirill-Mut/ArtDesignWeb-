from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Application
from .models import House, InternalPhoto, ExternalPhoto, Room
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
        fields = ['title', 'model_3d', 'description', 'total_area', 'effective_area', 'price', 'blueprint', 'main_photo']
        labels = {
            'title': 'Название дома',
            'model_3d': '3D модель',
            'description': 'Описание',
            'total_area': 'Общая площадь',
            'effective_area': 'Жилая площадь',
            'price': 'Цена',
            'blueprint': 'Схема дома',
            'main_photo': 'Основная фотография',
        }

class InternalPhotoForm(forms.ModelForm):
    class Meta:
        model = InternalPhoto
        fields = ['filename', 'house']
        labels = {
            'filename': 'Файл',
            'house': 'Дом',
        }

class ExternalPhotoForm(forms.ModelForm):
    class Meta:
        model = ExternalPhoto
        fields = ['filename', 'house']
        labels = {
            'filename': 'Файл',
            'house': 'Дом',
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'total_area', 'house']
        labels = {
            'name': 'Имя',
            'total_area': 'Общая площадь',
            'house': 'Дом',
        }