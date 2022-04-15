from django.conf import settings
from django.contrib import auth
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.forms import ContactsLoginForm, ContactsRegisterForm, ContactsForm

# Контроллер ауинтификации пользователя
from authapp.models import Contacts


def get_contact(request):
    contact = get_object_or_404(Contacts)
    return contact

# def get_contact(pk):
#     if settings.LOW_CACHE:
#         key = f'contact_{pk}'
#         contact = cache.get(key)
#         if contact is None:
#             contact = get_object_or_404(Contacts, pk=pk)
#             cache.set(key, contact)
#         return contact
#     else:
#         return get_object_or_404(Contacts, pk=pk)


def contact(request):
#     auth.get_user(request)
#     return HttpResponseRedirect(reverse('auth:registr'))

    #print(request.POST)

    title = 'контакт'
    content = {
        'title': title,
        'contact': Contacts.objects.filter(name=request.user),

    }
    print(f'content {content}')
    return render(request, 'authapp/contact.html', content)


def login(request):
    login_form = ContactsLoginForm(data=request.POST or None) # формирование формы авторизации

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))  # перекидывает на страницу по url 'main' все данные
            # из POST запроса. В шаблове обращаемся user

    content = {'title': 'Аутентификация', 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


# контроллер регистрации пользователя
def register(request):
    if request.method == 'POST':
        register_form = ContactsRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            # data_img = request.FILES.get('avatar')
            # print(data_img)
            register_form.save()

            # if send_verify_email(user):
            #     print('Send email success')
            # else:
            #     print('Send email error')
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ContactsRegisterForm()

    content = {'title': 'Регистрация', 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


# def send_verify_email(user):
#     verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
#     subject = "Подтверждение учетной записи"
#     message = f'{settings.DOMAIN_NAME}{verify_link}'
#
#     return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
#
#
# def verify(request, email, activation_key):
#     user = Contact.objects.get(email=email)
#     if user.activation_key == activation_key and not user.is_activation_key_expire():
#         user.is_active = True
#         user.activation_key = ''
#         user.save()
#         auth.login(request, user)
#     return render(request, 'authapp/verification.html')


def logout(request):
    pass

# Create your views here.
