# Generated by Django 2.2.4 on 2020-11-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(verbose_name='Новостройка'),
        ),
    ]
