from django.db import models

class Species(models.Model):
    region  = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=96, blank=True)
    full_desc = models.TextField(verbose_name='полное описание', blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(verbose_name='cтоимость', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='в наличии', default=0)
