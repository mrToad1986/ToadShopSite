from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import ShopUserRegisterForm

def register (request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
    if register_form.is_valid():
        register_form.save()
        return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)
