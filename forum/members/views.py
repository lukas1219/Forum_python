from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import registieren
from .models import forum


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registrierung(request):
    template = loader.get_template('registrierung.html')
    return HttpResponse(template.render({}, request))
  
def profil(request):
    template = loader.get_template('profil.html')
    return HttpResponse(template.render({}, request))  
  
def profil(request):
  profil = registieren.objects.all().values()
  template = loader.get_template('profil.html')
  context = {
    'profil': profil,
  }
  return HttpResponse(template.render(context, request))

def addrecord(request):
  u = request.POST['benutzername']
  v = request.POST['email']
  w = request.POST['firstname']
  x = request.POST['lastname']
  y = request.POST['password']
  z = request.POST['repeatpassword']
  daten = registieren(benutzername=u, email=v, firstname=w, lastname=x, password=y, repeatpassword=z)
  daten.save()
  return HttpResponseRedirect(reverse('profil'))

