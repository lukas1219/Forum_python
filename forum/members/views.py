from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registrierung(request):
    template = loader.get_template('registrierung.html')
    return HttpResponse(template.render({}, request))
  
def profil(request):
    template = loader.get_template('profil.html')
    return HttpResponse(template.render({}, request))  
