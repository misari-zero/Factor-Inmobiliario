# Generated by Django 3.2.11 on 2022-02-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_puesto_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='type',
            field=models.CharField(default=2, max_length=150, verbose_name='Tipo de Puesto'),
            preserve_default=False,
        ),
    ]
