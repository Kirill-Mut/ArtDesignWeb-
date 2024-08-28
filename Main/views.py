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
from .models import House
from .forms import HouseForm 

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















def house_list(request):
    houses = House.objects.all()
    return render(request, 'house_list.html', {'houses': houses})

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'house_detail.html', {'house': house})

def house_create(request):
    if request.method == "POST":
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('house_list')
    else:
        form = HouseForm()
    return render(request, 'house_form.html', {'form': form})

def house_update(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == "POST":
        form = HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house_detail', pk=house.pk)
    else:
        form = HouseForm(instance=house)
    return render(request, 'house_form.html', {'form': form})

def house_delete(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == "POST":
        house.delete()
        return redirect('house_list')
    return render(request, 'house_confirm_delete.html', {'house': house})

