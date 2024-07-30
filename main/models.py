from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacto(models.Model):
    nombre= models.CharField(max_length=255)
    email = models.EmailField()
    mensaje = models.TextField(max_length=3000)
    
    def __str__(self):
        return f'{self.nombre}'
    
    
class UserProfile(models.Model):
    roles =('administrador', 'Administrador'), ('paciente', 'Paciente')
    user = models.OneToOneField(User, related_name='usuario', on_delete = models.CASCADE)
    rol = models.CharField(max_length=255, choices=roles, default='paciente')
    
    
    
    
    
    
    
    
class CentroMedico(models.Model):
    nombre= models.CharField(max_length=255)
    def __str__(self):
        return f'{self.nombre}'
    
class Especialista(models.Model):
    nombre= models.CharField(max_length=255)
    def __str__(self):
        return f'{self.nombre}'