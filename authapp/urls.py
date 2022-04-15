from django.urls import path

import authapp.views as authapp

app_name = 'auth'

urlpatterns = [
    path('contact/', authapp.contact, name='contact'),
    path('login/', authapp.login, name='login'),
    path('registr/', authapp.register, name='registr'),
    #path('verify/<email>/<activation_key>', authapp.verify, name='verify')
    # path('logout/', authapp.logout, name='logout'),
]
