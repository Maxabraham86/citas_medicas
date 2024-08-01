
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from agendas.views import agendas, AgendaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include ('django.contrib.auth.urls'),name='login'),
    path('', include('main.urls')),
    path('agendas/', agendas, name='agendas'),
    path('agendas/nueva', AgendaView.as_view(), name='nueva_agenda')

]
