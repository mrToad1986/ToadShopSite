from django.db import models

class ListOfCountries (models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активно', default=True)

    def __str__(self):
        return self.name

class Regions(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

class Species(models.Model):
    pass

class Genus(models.Model):
    pass

class Feed(models.Model):
    pass
