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
from .models import House, InternalPhoto, ExternalPhoto, Room
from .forms import HouseForm, InternalPhotoForm, ExternalPhotoForm, RoomForm
from .models import Contacts
from .forms import ContactsForm


def base(request):
    houses = House.objects.all()
    return render(request, 'base.html', {'houses': houses})


def projects(request):
    return render(request, 'projects/projects.html')

def contacts(request):
    return render(request, 'contacts/contacts.html')

def about_us(request):
    return render(request, 'about_us/about_us.html')

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

def contacts_create(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContactsForm()
    return render(request, 'administration/contacts_form.html', {'form': form})

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

def contacts_delete(request, pk):
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('contacts_list')
    return render(request, 'administration/contacts_confirm_delete.html', {'contact': contact})



def house_list(request):
    houses = House.objects.all()
    return render(request, 'administration/house_list.html', {'houses': houses})

def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    return render(request, 'administration/house_detail.html', {'house': house})

def house_create(request):
    if request.method == 'POST':
        house_form = HouseForm(request.POST, request.FILES)

        # Получаем данные для фотографий и комнат
        internal_photos = request.FILES.getlist('internal_photos[]')
        external_photos = request.FILES.getlist('external_photos[]')
        room_names = request.POST.getlist('room_names[]')
        room_areas = request.POST.getlist('room_areas[]')

        if house_form.is_valid():
            house = house_form.save()

            # Сохранение внутренних фотографий
            for photo in internal_photos:
                InternalPhoto.objects.create(filename=photo, house=house)

            # Сохранение внешних фотографий
            for photo in external_photos:
                ExternalPhoto.objects.create(filename=photo, house=house)

            # Сохранение комнат
            for name, area in zip(room_names, room_areas):
                if name and area:  # Проверяем, что поля не пустые
                    Room.objects.create(name=name, total_area=area, house=house)

            return redirect('house_list')  # Перенаправляем на список домов
    else:
        house_form = HouseForm()

    return render(request, 'administration/house_create.html', {
        'house_form': house_form,
    })

def house_edit(request, house_id):
    house = get_object_or_404(House, id=house_id)

    if request.method == 'POST':
        house_form = HouseForm(request.POST, request.FILES, instance=house)

        # Получаем данные для фотографий и комнат
        internal_photos = request.FILES.getlist('internal_photos[]')
        external_photos = request.FILES.getlist('external_photos[]')
        room_names = request.POST.getlist('room_names[]')
        room_areas = request.POST.getlist('room_areas[]')
        internal_photo_ids = request.POST.getlist('internal_photo_ids[]')
        external_photo_ids = request.POST.getlist('external_photo_ids[]')

        if house_form.is_valid():
            house = house_form.save()

            # Обработка внутренних фотографий
            for i, photo_id in enumerate(internal_photo_ids):
                if i < len(internal_photos) and internal_photos[i]:  # Если загружен новый файл
                    internal_photo = InternalPhoto.objects.get(id=photo_id)
                    internal_photo.filename = internal_photos[i]  # Заменяем файл
                    internal_photo.save()

            # Обработка внешних фотографий
            for i, photo_id in enumerate(external_photo_ids):
                if i < len(external_photos) and external_photos[i]:  # Если загружен новый файл
                    external_photo = ExternalPhoto.objects.get(id=photo_id)
                    external_photo.filename = external_photos[i]  # Заменяем файл
                    external_photo.save()

            # Сохранение комнат
            Room.objects.filter(house=house).delete()  # Удаляем старые комнаты
            for name, area in zip(room_names, room_areas):
                if name and area:  # Проверяем, что поля не пустые
                    Room.objects.create(name=name, total_area=area, house=house)

            return redirect('house_list')
    else:
        house_form = HouseForm(instance=house)

    # Получаем фотографии и комнаты для отображения в шаблоне
    internal_photos = house.internal_photos.all()
    external_photos = house.external_photos.all()
    rooms = house.rooms.all()

    return render(request, 'administration/house_edit.html', {
        'house': house,
        'house_form': house_form,
        'internal_photos': internal_photos,
        'external_photos': external_photos,
        'rooms': rooms,
    })

def house_delete(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == "POST":
        house.delete()
        return redirect('house_list')
    return render(request, 'administration/house_confirm_delete.html', {'house': house})

