# accounts/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my/$', views.my_view, name='accounts.my'),
    url(r'^login/$', views.login_users_view, name='accounts.login'),
    url(r'^signup/$', views.signup_users_view, name='accounts.signup'),
    url(r'^logout/$', views.logout_users_view, name='accounts.logout'),
]