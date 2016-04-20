# accounts/views.py

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.fields import Empty
from django.shortcuts import redirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .forms import RegistroUserForm
from .models import UserProfile


@login_required
def my_view(request):
    return render(request, 'web/my.html')


def login_users_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('accounts.my')) # ??
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        #messages.success(request, 'Te has registrado correctamente.')
        if user is not None: # si EXISTE el usuario
            #print("Si el usuario NO existe")
            
            if user.is_active:
                login(request, user)
                return redirect(reverse('accounts.my'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                #return messages.add_message(request, messages.error, "lOGED!")
                pass
        else: 
            messages.error(request, 'El usuario o el password son incorrectos. Intentalo de nuevo.')
            return render_to_response('web/login.html', {}, RequestContext(request, {}))
                
    return render_to_response('web/login.html', RequestContext(request, {}))


def signup_users_view(request):
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = RegistroUserForm(request.POST)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            #photo = cleaned_data.get('photo')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # Añadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # y le asignamos la photo (el campo, permite datos null)
            #user_profile.photo = photo
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina accounts/gracias.html
            # Pero lo hacemos con un redirect.
            messages.success(request, 'Te has registrado correctamente.')
            #return render(request, 'accounts.login', {'username': username})
            return redirect(reverse('accounts.login'))
            #return redirect(reverse('accounts.login', kwargs={'username': username}))
        #else:
            #if User.objects.filter(username=form.cleaned_data['username']).exists():
                #del form.cleaned_data['username']
                #return messages.error(request, "duplicado")
            #return form.cleaned_data
            #messages.error(request, form.errors.as_json(escape_html=True))
            #return render_to_response('web/signup.html', {}, RequestContext(request, {}))
            #if cleaned_data.get('email') is Empty:
            #    messages.error(request, 'Rellena los campos vacíos.')
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = RegistroUserForm()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'web/signup.html', context)

def logout_users_view(request):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect(reverse('accounts.login'))
