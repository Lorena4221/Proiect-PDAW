from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import FilmForm
from .models import Film
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)  # Logare automată după înregistrare
            return redirect('home')  # Schimbă cu numele rutei tale
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

@login_required
def home(request):
    filme = Film.objects.all()
    return render(request, "home.html", {'filme': filme})

def noutati(request):
    return render(request, "news.html")

def reserve(request):
    return render(request, "reserve.html")

def contact(request):
    return render(request, "contact.html")


@user_passes_test(is_admin)
def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_film')
    else:
        form = FilmForm()
    filme = Film.objects.all()
    return render(request, 'add_film.html', {'form': form, 'filme': filme})

def delete_film(request, title):
    try:
        filme = Film.objects.get(title=title)
        filme.delete()
        return redirect('add_film')
    except Film.DoesNotExist:
        return HttpResponse("Film not found.")