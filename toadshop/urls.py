"""
URL configuration for toadshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', include('adminapp.urls', namespace='admin')) #добавить свою админку
    path('', mainapp.main, name='main'), # переход на главную страницу запускает контроллер views.main() в других проектах он же views.index
    path('category/', include('mainapp.urls', namespace='category')), #после category/ идет путь из mainapp.urls - то есть species и products
    path('auth/', include('authapp.urls', namespace='auth')), #после auth/ идет путь из authapp.urls - то есть login, register, logout
    #path('basket/', include('basketapp.urls', namespace='basket')),
    #path('order/', include('ordersapp.urls', namespace='order')),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
