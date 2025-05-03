from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import FilmForm
from .models import Film

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

@login_required
def home(request):
    filme = Film.objects.all()
    return render(request, "home.html", {'filme': filme})

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
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