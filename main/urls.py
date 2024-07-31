from django.urls import path
from main.views import register, contacto, inicio, ContactoView, RegistroView

urlpatterns = [

        path('', inicio, name='inicio' ),
        path('register/', register, name ='register'),
        path('contacto', contacto, name = 'contacto'),
        path('contact', ContactoView.as_view(), name = 'contact'),
        path('registro', RegistroView.as_view(), name='registro')

]