"""
Definition of urls for django_demo.
"""

from datetime import datetime
from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
#from app import forms, views
from HelloDjangoApp import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^home$', views.index, name='home'),

    path('', views.index, name='home'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    #path('login/',
    #     LoginView.as_view
    #     (
    #         template_name='app/login.html',
    #         authentication_form=forms.BootstrapAuthenticationForm,
    #         extra_context=
    #         {
    #             'title': 'Log in',
    #             'year' : datetime.now().year,
    #         }
    #     ),
    #     name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('admin/', admin.site.urls),
]
