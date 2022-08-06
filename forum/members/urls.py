from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrierung/', views.registrierung, name='registrierung'),
    path('theaser/', views.theaser, name='theaser'),
    path('profil/', views.profil, name='profil'),
    path('impressum/', views.impressum, name='impressum'),
    path('registrierung/addrecord/', views.addrecord, name='addrecord'),
    path('profil/update/<int:id>', views.update, name='update'),
    path('profil/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('newtheaser/', views.newtheaser, name='newtheaser'),
]