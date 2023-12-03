from django.urls import path
import toadshop.mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.accomodations, name='index'),
    path('accommodation_details/<int:pk>/', mainapp.accommodation, name='accommodation'),
]
