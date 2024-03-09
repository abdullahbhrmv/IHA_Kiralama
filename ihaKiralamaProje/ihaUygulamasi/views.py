# ihaUygulamasi/views.py

from .models import IHA, Kiralama
from .forms import IHAForm, KiralamaForm, CustomUserCreationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    # Eğer kullanıcı oturum açmışsa, headerda kullanıcı adını göster
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'home.html', {'username': username})
    else:
        return render(request, 'home.html')

def iha_list(request):
    iha_list = IHA.objects.all()
    return render(request, 'ihaList/iha_list.html', {'iha_list': iha_list})

def iha_detail(request, iha_id):
    iha = get_object_or_404(IHA, pk=iha_id)
    return render(request, 'ihaList/iha_detail.html', {'iha': iha})

def iha_create(request):
    if request.method == 'POST':
        form = IHAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IHAForm()
    return render(request, 'ihaList/iha_create.html', {'form': form})

def iha_update(request, iha_id):
    iha = get_object_or_404(IHA, pk=iha_id)
    if request.method == 'POST':
        form = IHAForm(request.POST, instance=iha)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IHAForm(instance=iha)
    return render(request, 'ihaList/iha_update.html', {'form': form, 'iha': iha})

def iha_delete(request, iha_id):
    iha = get_object_or_404(IHA, pk=iha_id)
    iha.delete()
    return redirect('iha_list')

def kiralama_list(request):
    kiralama_list = Kiralama.objects.all()
    return render(request, 'ihaKirala/kiralama_list.html', {'kiralama_list': kiralama_list})

def kiralama_detail(request, kiralama_id):
    kiralama = get_object_or_404(Kiralama, pk=kiralama_id)
    return render(request, 'ihaKirala/kiralama_detail.html', {'kiralama': kiralama})

def kiralama_create(request):
    if request.method == 'POST':
        form = KiralamaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kiralama_list')
    else:
        form = KiralamaForm()
    return render(request, 'ihaKirala/kiralama_create.html', {'form': form})

def kiralama_update(request, kiralama_id):
    kiralama = get_object_or_404(Kiralama, pk=kiralama_id)
    if request.method == 'POST':
        form = KiralamaForm(request.POST, instance=kiralama)
        if form.is_valid():
            form.save()
            return redirect('kiralama_list')
    else:
        form = KiralamaForm(instance=kiralama)
    return render(request, 'ihaKirala/kiralama_update.html', {'form': form, 'kiralama': kiralama})

def kiralama_delete(request, kiralama_id):
    kiralama = get_object_or_404(Kiralama, pk=kiralama_id)
    kiralama.delete()
    return redirect('kiralama_list')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return JsonResponse({'success': True, 'redirect': '/'})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@require_POST
def register_user(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        auth_login(request, user)
        return JsonResponse({'success': True, 'redirect': '/'})
    else:
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})

def logout(request):
    auth_logout(request)
    return redirect('home')
