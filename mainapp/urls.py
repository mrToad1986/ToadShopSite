from django.urls import path
from mainapp import views as mainapp

# имя приложения
app_name = 'mainapp'

urlpatterns = [
    # вывод предложений по (двум) основным катеригоиям
    path('species/', mainapp.species, name='species'),
    path('products/', mainapp.products, name='products'),
    # вывод подробного по животному
    path('species_detailed/<int:pk>/', mainapp.species_detailed, name='species_detailed'),
    # int:pk идентификатор записи, который будет передаваться в HTML-шаблоне
    path('products_detailed/<int:pk>/', mainapp.species_detailed, name='products_detailed'),
    # int:pk идентификатор записи, который будет передаваться в HTML-шаблоне
]
