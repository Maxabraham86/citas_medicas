from django.contrib import admin
from agendas.models import CentroMedico, Especialista

# Register your models here.
class CentroMedicoAdmin(admin.ModelAdmin):
    pass

class EspecialistaAdmin(admin.ModelAdmin):
    pass



admin.site.register(CentroMedico, CentroMedicoAdmin)
admin.site.register(Especialista, EspecialistaAdmin)