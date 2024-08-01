from django.db import models

# Create your models here.
class CentroMedico(models.Model):
    nombre= models.CharField(max_length=100)
    direccion= models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.nombre}'



class Especialista(models.Model):
    especialidades =(('neurocirugía', 'Neurocirugía'), ('dermatología', 'Dermatología'), ('psiquiatría', 'Psiquiatría'), ('medicina general', 'Medicina General'))
    nombre= models.CharField(max_length=100)
    especialidad= models.CharField(max_length=255, choices= especialidades)
    
    def __str__(self):
        return f'{self.nombre} ({self.id})'
    
class Agenda(models.Model):
    fecha_disponible= models.DateField()
    hora_disponible = models.TimeField()
    especialista= models.ForeignKey(Especialista, on_delete= models.RESTRICT, related_name='agendas')
    centro_medico= models.ForeignKey(CentroMedico, on_delete= models.RESTRICT, related_name='agendas')