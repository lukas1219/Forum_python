from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrierung/', views.registrierung, name='registrierung'),
    path('profil/', views.profil, name='profil'),
    path('registrierung/addrecord/', views.addrecord, name='addrecord'),
]