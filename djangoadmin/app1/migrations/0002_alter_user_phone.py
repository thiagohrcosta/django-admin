# Generated by Django 4.0.2 on 2024-03-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(verbose_name='phone'),
        ),
    ]