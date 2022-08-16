from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrierung/', views.registrierung, name='registrierung'),
    path('theaser_link/', views.theaser_link, name='theaser_link'),
    path('profil/', views.profil, name='profil'),
    path('impressum/', views.impressum, name='impressum'),
    path('registrierung/addrecord/', views.addrecord, name='addrecord'),
    path('profil/update/<int:id>', views.update, name='update'),
    path('profil/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('theaser_link/newtheaser/', views.newtheaser, name='newtheaser'),
    path('answer/<int:id>', views.answer, name='answer'),
    path('answer/theaseranswer/', views.theaseranswer, name='theaseranswer'),
]
