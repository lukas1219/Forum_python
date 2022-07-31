from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registrierung(request):
    template = loader.get_template('registrierung.html')
    return HttpResponse(template.render({}, request))
  
def profil(request):
    template = loader.get_template('profil.html')
    return HttpResponse(template.render({}, request))  
  
def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def addrecord(request):
  u = request.POST['benutzername']
  v = request.POST['email']
  w = request.POST['firstname']
  x = request.POST['lastname']
  y = request.POST['password']
  z = request.POST['repeatpassword']
  member = Members(benutzername=u, email=v, firstname=w, lastname=x, password=y, repeatpassword=z)
  member.save()
  return HttpResponseRedirect(reverse('index'))
