from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse #позволяет по имени view получить его url.
from django.contrib import auth
from .forms import ShopUserRegisterForm, ShopUserLoginForm, ShopUserProfileEditForm, ShopUserEditForm

def register (request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    content = {
        'title': title,
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', content)


def login(request):
    title = 'вход'
    login_form = ShopUserLoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else '' #перенаправление на форму аутентификации
    if request.method == 'POST' and login_form.is_valid():
        nickname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(nickname=nickname, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))
    content = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def edit():
    pass



