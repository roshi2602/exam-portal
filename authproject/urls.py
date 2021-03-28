"""authproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from auth1 import views
from django.contrib.auth import authenticate
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.homepageview, name='home'),
    path('java/', views.javaexamsview),
    path('python/', views.pythonexamsview),
    path('aptitude/', views.aptitudeexamsview),
    path('maths/', views.mathsexamsview),
    path('acn/', views.acnexamsview),
    path('online/', views.onlinexamsview),
    path('quiz/', views.quizexamsview),
    path('start/', views.paperexamsview),
    #path('login/', views.loginexamsview),
    #path('logout/', views.logoutview),
    path('signup/', views.signupview),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

