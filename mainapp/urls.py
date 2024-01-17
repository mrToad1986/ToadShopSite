from django.urls import path
from mainapp import views as mainapp

# имя приложения
app_name = 'mainapp'

urlpatterns = [
    # вывод вообще всех предложений
    path('', mainapp.species, name='index'),

    # вывод подробного одного предложения
    path('species_detailed/<int:pk>/', mainapp.species_detailed, name='species_detailed')
    # идентификатор записи, который будет передаваться в HTML-шаблоне
]
