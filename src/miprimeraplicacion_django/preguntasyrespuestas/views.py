#from django.http import HttpResponse, Http404

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response
import json

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from preguntasyrespuestas.models import Pregunta
from preguntasyrespuestas.models import SignUpForm


def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            #first_name = form.cleaned_data["first_name"]
            #last_name = form.cleaned_data["last_name"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            #user.first_name = first_name
            #user.last_name = last_name
 
            # Save new user attributes
            user.save()
 
            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('web/signup.html', data, context_instance=RequestContext(request))

# Create your views here.


def index_view(request):
    return render_to_response('web/index.html',{}, context_instance=RequestContext(request))
    

def faq_view(request):
    return render_to_response('web/faq.html')

def info_view(request):
    # Comprobar si en la misma pagina hay uno en formato libre!!!!
    # se podria comprobar en el fichero general?!?!?!?! coincidiendo url y nombre ?!??!?!?!?!??!!?
    # Archivo JSON con los datos recogidos
    objs = json.loads("[%s]"%(open('/home/dru/workspace/gedea/src/miprimeraplicacion_django/static/dataULL.json').read().replace('}{', '},{')))
    json_data = json.dumps(objs)
    item_dict = json.loads(json_data)

    #print item_dict[0][0]['Extension']      == .pdf
    #print len(objs[0])                      == 47

    positive = 0;
    negative = 0;
    for i in range(len(objs[0])):
        if item_dict[0][i]['Extension'] == ".pdf":
            positive=positive+1
        if item_dict[0][i]['Extension'] == ".odt":
            negative=negative+1
        if item_dict[0][i]['Extension'] == ".docx":
            negative=negative+1
        if item_dict[0][i]['Extension'] == ".doc":
            negative=negative+1
        if item_dict[0][i]['Extension'] == ".ppt":
            negative=negative+1
    return render_to_response('web/info.html', {'positive': positive , 'negative': negative})

def error(request):
    questions = Pregunta.objects.all()
    return render_to_response('web/404.html', {'questions': questions})

@login_required()
def my(request):
    questions = Pregunta.objects.all()
    return render_to_response('web/my.html', {'questions': questions})


def login(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('my'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('main'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        mensaje = 'Nombre de usuario o contraseña no valido'

    return render_to_response('web/login.html', {'mensaje': mensaje})
    '''
    
    answer_str = "Preguntas <br/>"
    answer_str += '<br/>'.join(["id: %s, asunto: %s, descripcion: %s, fecha: %s"%
    (p.id, p.asunto, p.descripcion, p.fecha_publicacion ) for p in questions])
    return HttpResponse(answer_str)
    '''
    
    #return HttpResponse("Estamos creando nuestra primera view!!")
    
'''
def pregunta_detalle(request, pregunta_id):
    try:
        questions = Pregunta.objects.get(pk=pregunta_id)
    except Pregunta.DoesNotExist:
        raise Http404
    return HttpResponse("%s?" % questions.asunto)
'''

def pregunta_detalle(request, pregunta_id):
    question = get_object_or_404(Pregunta, pk=pregunta_id)
    return render_to_response('preguntasyrespuestas/pregunta_detalle.html', {'question': question})
     
    '''
    return HttpResponse("%s?" % questions.asunto)
    '''