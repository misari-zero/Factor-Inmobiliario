# Generated by Django 3.2.11 on 2022-02-07 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='descripcion',
        ),
    ]