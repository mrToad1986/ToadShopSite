from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Category, Species, Product


def main(request):
    content = {
        'title': 'AmphiDelights',
        'date': datetime.now(),
    }
    return render(request, 'mainapp/index.html', content)


# установить django-stubs или использовать models.Manager()
def species(request):
    title = 'животные'
    list_of_species = Species.objects.all()
    content = {
        'title': title,
        'list_of_species': list_of_species,
    }
    return render(request, 'mainapp/species.html', content)


def products(request):
    pass

def species_detailed(request, pk):
    title = 'животные'
    content = {
        'title': title,
        'details': get_object_or_404(Species, pk=pk),
    }
    return render(request, 'mainapp/species_detailed.html', content)

def products_detailed(requet):
    pass