from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.forms import ContactForm
from main.services import crear_user

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

def contacto(request):
    if request.method == 'GET':
        form = ContactForm()                   
        context = {'form': form}               
        return render(request, 'contacto.html', context)
    else:
        form = ContactForm(request.POST)        
        if form.is_valid():                     
            contacto.objects.create(
                **form.cleaned_data
            )                                   
            return redirect('/success')         
        context = {'form': form}                
        return render(request, 'contacto.html', context) 


# test solicita que el usuario requiere no estar autentificado

def usuario_no_autentificado(user):
    # retorna un usuario no  autentificado
    return not user.is_authenticated

@user_passes_test(usuario_no_autentificado) # eñ 
def register(request):
    if request.method == 'POST':
        id= request.POST ['username']
        # first_name= request.POST['first_name']
        email = request.POST ['email']
        password = request.POST['password']
        pass_confirm = request.POST ['pass_confirm']
        crear_user(
            request, id , email, password, pass_confirm)
        return redirect('/accounts/login')
        
    else:
        return render(req, 'register.html')
        