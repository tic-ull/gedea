"""django_miprimeraplicacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from django.conf.urls import patterns, url, include
from django.contrib.auth.views import login

import django_cas.views
import preguntasyrespuestas.views


urlpatterns = [
               
    # URLs de la APP accounts
    url(r'^accounts/', include('accounts.urls')),
    
     # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
    url(r'^error/$', preguntasyrespuestas.views.error, name='questions'),
    #url(r'^login/$', preguntasyrespuestas.views.login, name='login'),


    #url(r'^signup/$', preguntasyrespuestas.views.signup, name='signup'),
    url(r'^faq/$', preguntasyrespuestas.views.faq_view, name='faq'),
    
    url(r'^info/$', preguntasyrespuestas.views.info_view, name='info'),
    #url(r'^my/$', preguntasyrespuestas.views.my, name='my'),
    url(r'^$', preguntasyrespuestas.views.index_view, name='main'),
    url(r'helpdesk/', include('helpdesk.urls')),
    #url(r'^preguntas/(?P<pregunta_id>\d+)/$','preguntasyrespuestas.views.pregunta_detalle', name='pregunta_detalle'),
    
    #===========================================
    # django-cas CONFIGURATION  
    #===========================================
    # https://bitbucket.org/cpcc/django-cas/
    #===========================================
    url(r'^cas/$', django_cas.views.login, name='cas'),
    #url(r'^accounts/logout/$', django_cas.views.logout),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
