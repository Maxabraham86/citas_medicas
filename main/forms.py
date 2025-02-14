from django import forms
from django.forms import ModelForm
from main.models import Contacto

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label='Nombre:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese nombre aquí'
        })
    )
    email = forms.EmailField(
        max_length=100,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3 fst-italic w-3',
            'placeholder': 'Ingrese correo aquí'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje:',
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3 fst-italic',
            'rows': 5,
            'placeholder': 'Ingrese mensaje. Máximo 500 carácteres'
        })
    )
    
class ContactoModelForm(ModelForm):
    class Meta:
        model= Contacto
        fields=['nombre', 'email' , 'mensaje']