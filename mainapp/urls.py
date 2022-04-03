from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('login/', mainapp.login, name='login'),
    path('logout/', mainapp.logout, name='logout'),
    ]
