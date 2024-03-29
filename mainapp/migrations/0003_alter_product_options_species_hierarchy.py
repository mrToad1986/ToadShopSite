# Generated by Django 4.2.7 on 2024-02-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_species_options_product_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AddField(
            model_name='species',
            name='hierarchy',
            field=models.CharField(blank=True, choices=[('A', 'амфибия'), ('R', 'рептилия'), ('I', 'насекомое')], max_length=12, verbose_name='класс'),
        ),
    ]
