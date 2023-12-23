from django.db import models
from django.db.models import CharField


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, )
    description = models.TextField(blank=True, null=True, verbose_name='описание категории')

    def __str__(self):
        return self.name


class Species(models.Model):
    AMPHIBIAN = 'A'
    REPTILE = 'R'
    INSECT = 'I'

    Hierarchy_class = (
        (AMPHIBIAN, 'амфибия'),
        (REPTILE, 'рептилия'),
        (INSECT, 'насекомое')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True, verbose_name='название')
    short_desc = models.CharField(max_length=96, blank=True, verbose_name='краткое описание')
    full_desc = models.TextField(blank=True, verbose_name='полное описание')
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='cтоимость')
    quantity = models.PositiveIntegerField(default=0, verbose_name='в наличии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'животное'
        verbose_name_plural = 'животные'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True, verbose_name='название')
    short_desc = models.CharField(max_length=96, blank=True, verbose_name='краткое описание')
    full_desc = models.TextField(blank=True, verbose_name='полное описание')
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='cтоимость')
    quantity = models.PositiveIntegerField(default=0, verbose_name='в наличии')