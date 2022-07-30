from django.db import models

class registieren(models.Model):
    
    benutzername = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    repeatpassword = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.id) + ' ' + self.benutzername + ' ' + self.email + ' ' + self.firstname + ' ' + self.lastname + ' ' + self.password + ' ' + self.repeatpassword
    