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
  
def update(request, id):
    profil = registieren.objects.get(id=id)
    template = loader.get_template('profil_bearbeiten.html')
    context = {
      'profil' : profil,
    }
    return HttpResponse(template.render(context, request))

  
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
  return HttpResponseRedirect(reverse('index'))

def updaterecord(request, id):
  benutzername = request.POST['benutzername']
  email = request.POST['email']
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  password = request.POST['password']
  repeatpassword = request.POST['repeatpassword']
  daten = registieren.objects.get(id=id)
  daten.benutzername = benutzername
  daten.email = email
  daten.firstname = firstname
  daten.lastname = lastname
  daten.password = password
  daten.repeatpassword = repeatpassword
  daten.save()
  return HttpResponseRedirect(reverse('profil'))