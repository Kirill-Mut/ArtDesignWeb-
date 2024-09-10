from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import login
from django.conf import settings
User = settings.AUTH_USER_MODEL
from .forms import RegistrationForm
from django.core.mail import send_mail
from .forms import ApplicationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import House
from .forms import HouseForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import House
from .forms import HouseForm
from django.shortcuts import render, redirect
from .forms import HouseForm
from .models import House
from .forms import HouseForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import House, ExteriorPhoto, InteriorPhoto, Room
from .forms import HouseForm, ExteriorPhotoForm, InteriorPhotoForm, RoomForm, ExteriorPhotoFormSet, InteriorPhotoFormSet,RoomFormSet
from .models import Contacts
from .forms import ContactsForm
from .models import House, ExteriorPhoto, InteriorPhoto, Room
from .forms import HouseForm, ExteriorPhotoForm, InteriorPhotoForm, RoomForm

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'registration/login.html')



def registration_view(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST or None, request=request)
        if registration_form.is_valid():
            username = registration_form.cleaned_data['username']
            # Проверка, существует ли уже пользователь с таким именем
            if User.objects.filter(username=username).exists():
                error_message = 'Пользователь с таким именем уже существует'
                context = {'registration_form': registration_form, 'error_message': error_message}
                return render(request, 'registration/registration.html', context)
            else:
                registration_form.save()
                return redirect('base')
    else:
        registration_form = RegistrationForm()
    context = {'registration_form': registration_form}

    return render(request, 'registration/registration_login.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
    else:
        form = LoginForm()
        context = {'form': form}

    return render(request, 'registration/registration_login.html', context)

def registration_login_view(request):
    context = {'registration_form': RegistrationForm(), 'form': LoginForm()}
    if request.method == 'POST':
        # Обработка регистрации
        if 'register' in request.POST:
            registration_form = RegistrationForm(request.POST or None, request=request)
            if registration_form.is_valid():
                registration_form.save()
                return redirect('base')
            else:
                context['registration_form'] = registration_form
            return render(request, 'registration/registration_login.html', context)
        # Обработка входа в систему
        elif 'login' in request.POST:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('base')
            context['form'] = form
            return render(request, 'registration/registration_login.html', context)
    return render(request, 'registration/registration_login.html', context)





def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            send_mail(
                'Новая заявка',
                f'Имя: {application.name}\nТелефон: {application.phone}\nEmail: {application.email}\nСообщение: {application.message}',
                'bublichenko.nik@mail.ru',  # email
                ['bublichenko.nik@mail.ru'],  # email администратора
                fail_silently=False,
            )
            return redirect('base')  
    else:
        form = ApplicationForm()
    
    return render(request, 'application_form.html', {'form': form})








def contacts_list(request):
    contacts = Contacts.objects.all()
    return render(request, 'administration/contacts_list.html', {'contacts': contacts})

# Функция для создания нового контакта
def contacts_create(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContactsForm()
    return render(request, 'administration/contacts_form.html', {'form': form})

# Функция для редактирования существующего контакта
def contacts_update(request, pk):
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method == "POST":
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContactsForm(instance=contact)
    return render(request, 'administration/contacts_form.html', {'form': form})

# Функция для удаления контакта
def contacts_delete(request, pk):
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('contacts_list')
    return render(request, 'administration/contacts_confirm_delete.html', {'contact': contact})






def house_list(request):
    houses = House.objects.all()
    return render(request, 'administration/house_list.html', {'houses': houses})

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'administration/house_detail.html', {'house': house})

def house_create(request):
    if request.method == "POST":
        house_form = HouseForm(request.POST, request.FILES)
        exterior_photo_formset = ExteriorPhotoFormSet(request.POST, request.FILES)
        interior_photo_formset = InteriorPhotoFormSet(request.POST, request.FILES)
        room_formset = RoomFormSet(request.POST)

        if house_form.is_valid() and exterior_photo_formset.is_valid() and interior_photo_formset.is_valid() and room_formset.is_valid():
            house = house_form.save()

            # Сохранение внешних фотографий
            exterior_photos = exterior_photo_formset.save(commit=False)
            for photo in exterior_photos:
                photo.house = house
                photo.save()

            # Сохранение внутренних фотографий
            interior_photos = interior_photo_formset.save(commit=False)
            for photo in interior_photos:
                photo.house = house
                photo.save()

            # Сохранение комнат
            rooms = room_formset.save(commit=False)
            for room in rooms:
                room.house = house
                room.save()

            return redirect('house_list')
    else:
        house_form = HouseForm()
        exterior_photo_formset = ExteriorPhotoFormSet(queryset=ExteriorPhoto.objects.none())
        interior_photo_formset = InteriorPhotoFormSet(queryset=InteriorPhoto.objects.none())
        room_formset = RoomFormSet(queryset=Room.objects.none())

    return render(request, 'administration/house_form.html', {
        'house_form': house_form,
        'exterior_photo_formset': exterior_photo_formset,
        'interior_photo_formset': interior_photo_formset,
        'room_formset': room_formset,
    })

def house_update(request, pk):
    house = get_object_or_404(House, pk=pk)
    
    room_formset = RoomFormSet(instance=house)
    exterior_photo_formset = ExteriorPhotoFormSet(instance=house)
    interior_photo_formset = InteriorPhotoFormSet(instance=house)
    
    if request.method == "POST":
        house_form = HouseForm(request.POST, request.FILES, instance=house)
        room_formset = RoomFormSet(request.POST, instance=house)
        exterior_photo_formset = ExteriorPhotoFormSet(request.POST, request.FILES, instance=house)
        interior_photo_formset = InteriorPhotoFormSet(request.POST, request.FILES, instance=house)
        
        if house_form.is_valid() and room_formset.is_valid() and exterior_photo_formset.is_valid() and interior_photo_formset.is_valid():
            house = house_form.save()
            room_formset.save()
            exterior_photo_formset.save()
            interior_photo_formset.save()
            return redirect('house_detail', pk=house.pk)
    else:
        house_form = HouseForm(instance=house)
    
    return render(request, 'administration/house_form.html', {
        'house_form': house_form,
        'room_formset': room_formset,
        'exterior_photo_formset': exterior_photo_formset,
        'interior_photo_formset': interior_photo_formset,
    })

def house_delete(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == "POST":
        house.delete()
        return redirect('house_list')
    return render(request, 'administration/house_confirm_delete.html', {'house': house})

