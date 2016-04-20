from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
# Create your models here.
class Pregunta(models.Model):
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.asunto+self.descripcion
        
    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = 'Preguntado hoy?'
    
class Respuesta(models.Model):
    Pregunta = models.ForeignKey(Pregunta)
    contenido = models.TextField()
    mejor_respuesta = models.BooleanField("Respuesta preferida", default=False)
    
    def __str__(self):
        return self.contenido
    
class Busqueda(models.Model):
    url =  models.TextField()
    resultados = models.IntegerField()
    
    def __str__(self):
        return self.resultados
    
    
    
    