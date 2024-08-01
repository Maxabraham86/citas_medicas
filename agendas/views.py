from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from agendas.forms import AgendaModelForm
# Create your views here.


def es_administrador(user):
    if user.groups.filter(name='administradores').exists():
        return True
    else:
        return False


@login_required
def agendas(request):
    user = request.user
    es_un_administrador = es_administrador(user)
    context={
        'es_administrador': es_un_administrador
    }
    return render (request, 'agendas.html', context)


class AgendaView(View):
    # el siguiente codigo protege tanto el GET como el POST
    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args, **kwargs)
    
    # el GET carga el template
    def get(self,request):
        form = AgendaModelForm()
        context={
            'form': form
        }        
        return render(request, 'nueva_agenda.html', context)

    def post(self,request):
        form = AgendaModelForm(request.POST)
        nueva_agenda = form.save()
        messages.success(request, 'Agenda creada')
        return redirect('/agendas')
