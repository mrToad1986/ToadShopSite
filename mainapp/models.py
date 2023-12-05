from django.db import models

class ListOfCountries (models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активно', default=True)

    def __true__(self):
        return self.name
