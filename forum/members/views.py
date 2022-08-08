from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import registieren, forum

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registrierung(request):
    template = loader.get_template('registrierung.html')
    return HttpResponse(template.render({}, request))
    
def theaser(request):
  template = loader.get_template('new_theaser.html')
  return HttpResponse(template.render({}, request))

def profil(request):
    template = loader.get_template('profil.html')
    return HttpResponse(template.render({}, request))  
  
def impressum(request):
    template = loader.get_template('impressum.html')
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
  profil = registieren(benutzername=u, email=v, firstname=w, lastname=x, password=y, repeatpassword=z)
  profil.save()
  return HttpResponseRedirect(reverse('index'))

def updaterecord(request, id):
  benutzername = request.POST['benutzername']
  email = request.POST['email']
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  password = request.POST['password']
  repeatpassword = request.POST['repeatpassword']
  profil = registieren.objects.get(id=id)
  profil.benutzername = benutzername
  profil.email = email
  profil.firstname = firstname
  profil.lastname = lastname
  profil.password = password
  profil.repeatpassword = repeatpassword
  profil.save()
  return HttpResponseRedirect(reverse('profil'))

def forum(request):
  forum = forum.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'forum': forum,
  }
  return HttpResponse(template.render(context, request))


def newtheaser(request):
  s = request.POST['headline']
  t = request.POST['theaser_text']
  forum = forum(headline=s, theaser_text=t)
  forum.save()
  return HttpResponseRedirect(reverse('index'))