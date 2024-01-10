from django.urls import path
from mainapp import views as mainapp

# имя приложения
app_name = 'mainapp'

urlpatterns = [
    # вывод всех предложений по животным
    path('', mainapp.species, name='index'),
    # вывод подробного одного предложения
    path('species_detailed/<int:pk>/', mainapp.species_detailed, name='species_detailed')
]
