# Generated by Django 4.2.7 on 2024-01-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name': 'животное', 'verbose_name_plural': 'животные'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='в наличии'),
        ),
        migrations.AddField(
            model_name='species',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='в наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='species',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество'),
        ),
    ]