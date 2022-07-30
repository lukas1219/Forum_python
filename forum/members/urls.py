from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrierung/', views.registrierung, name='registrierung'),
]