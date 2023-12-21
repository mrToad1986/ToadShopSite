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
    region  = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=96, blank=True)
    full_desc = models.TextField(verbose_name='полное описание', blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(verbose_name='cтоимость', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='в наличии', default=0)

class Genus(models.Model):
    pass

class Feed(models.Model):
    pass

class User(models.Model):
    pass
