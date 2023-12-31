# Generated by Django 4.2.7 on 2023-12-22 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название')),
                ('short_desc', models.CharField(blank=True, max_length=96, verbose_name='краткое описание')),
                ('full_desc', models.TextField(blank=True, verbose_name='полное описание')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='cтоимость')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='в наличии')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название')),
                ('short_desc', models.CharField(blank=True, max_length=96, verbose_name='краткое описание')),
                ('full_desc', models.TextField(blank=True, verbose_name='полное описание')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='cтоимость')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='в наличии')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]
