from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.views import View
from django.contrib import messages
from main.forms import ContactForm
from main.services import crear_user
from main.models import Contacto
from main.forms import ContactoModelForm
# Create your views here.


def inicio(request):
    return render(request, 'index.html')



class ContactoView(View):
    def get(self, request):
        form = ContactoModelForm()
        context={
            'form':form
        }
        return render (request, 'contact.html', context)

    def post(self,request):
        #1. Recuperamos los datos del formulario
        form = CointactoModelForm(request.POST)
        #2. Guardamos en la BBDD
        form.save()
        #3. Damos feedback al usuario
        messages.succes(request, 'Contacto enviado!')
        #4. redirigimos
        return redirect('/')
    
    
def contacto(request):
    if request.method == 'GET':
        form = ContactForm()                   
        context = {'form': form}               
        return render(request, 'contacto.html', context)
    else:
        form = ContactForm(request.POST)        
        if form.is_valid():                     
            Contacto.objects.create(
                **form.cleaned_data
            )                                   
            return redirect('/')         
        context = {'form': form}                
        return render(request, 'contacto.html', context) 


# test solicita que el usuario requiere no estar autentificado

def usuario_no_autentificado(user):
    # retorna un usuario no  autentificado
    return not user.is_authenticated

@user_passes_test(usuario_no_autentificado) # eñ 
def register(request):
    if request.method == 'POST':
        username= request.POST ['email']
        email = request.POST ['email']
        password = request.POST['password']
        pass_confirm = request.POST ['pass_confirm']
        crear_user(
            username , email, password, pass_confirm)
        return redirect('/accounts/login')
        
    else:
        return render(request, 'register.html')
        
class RegistroView(View):
    def get(self,request):
        return render(request, 'registration/registro.html')
    def post(self, request):
        #1. recuperamos los datos del formulario
        email=request.POST['email']
        password=request.POST['password']
        pass_repeat=request.POST['pass_repeat']
        #2. validamos que contraseñas no se repitan
        if password != pass_repeat:
            messages.error(request,'Contraseñas no coinciden')
        return redirect('/registro') 
        #3. Creamos el usuario
        user = User.objects.create_user(username=email, email=email, password=password)
        #4. creamos (si es que no existe el grupo)
        group, creado_en =Group.objects.get_or_create(name='pacientes')
        #5. le asignamos el grupo al usuario
        user.groups.add(group)
        #6. feedback y redirigimos
        messages.success('Usuario Creado')
        return redirect('/')