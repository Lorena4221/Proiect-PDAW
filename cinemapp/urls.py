from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_film/', views.add_film, name='add_film'),
    path('delete/<str:title>/', views.delete_film, name='delete_film'),
]