from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacto(models.Model):
    nombre
    
    
    
    
    
    
    

class UserProfile(models.Model):
    roles =('administrador', 'Administrador'), ('paciente', 'Paciente')
    user = models.OneToOneField(User, related_name='username', on_delete = models.CASCADE)
    direccion = models.CharField(max_length= 255)
    telefono = models.CharField(max_length=255 , null=True, blank=True)
    rol = models.CharField(max_length=255, choices=roles, default='paciente')