from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mainapp.forms import ContactLoginForm


def login(request):
    login_form = ContactLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': 'Аутентификация', 'login_form': login_form}
    return render(request, 'mainapp/login.html', content)


def logout(request):
    pass

# Create your views here.
