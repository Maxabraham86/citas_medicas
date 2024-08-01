from django import forms
from django.forms import ModelForm
from agendas.models import Agenda


class AgendaModelForm(ModelForm):
    
    class Meta:
        model= Agenda
        fields=['fecha_disponible','hora_disponible', 'especialista','centro_medico',]
        
        widgets={
            'fecha_disponible': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'hora_disponible': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),
            'especialista':forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'centro_medico':forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
            
            }
        