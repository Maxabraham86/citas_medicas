from django.contrib.auth.models import User
from main.models import UserProfile



def crear_user(request,username, first_name, email, password, pass_confirm):
        #validamos que el password coincida
    if password !=pass_confirm:
        return False, 'las contraseñas no coinciden'
    
    #2 creamos objeto user
    try:
        user = User.objects.create_user(
            username= username,
            first_name = first_name,
            
            email= email,
            password=  password,
    )
    except IntegrityError:
        return False, 'Rut duplicado'
    #3 creamos el UserProfile
    
    