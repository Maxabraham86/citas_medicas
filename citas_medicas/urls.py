
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from main.views import register, contacto, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include ('django.contrib.auth.urls'),name='login'),
    path('', inicio, name='inicio' ),
    path('register/', register, name ='register'),
    path('contacto', contacto, name = 'contacto'),
]
