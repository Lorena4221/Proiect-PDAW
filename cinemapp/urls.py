from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.noutati, name='news'),
    path('reserve/', views.reserve, name='reserve'),
    path('contact/', views.contact, name='contact'),
    path('add_film/', views.add_film, name='add_film'),
    path('delete/<str:title>/', views.delete_film, name='delete_film'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)