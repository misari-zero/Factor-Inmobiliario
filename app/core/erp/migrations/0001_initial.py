# Generated by Django 3.2.11 on 2022-01-31 21:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Área')),
                ('descripcion', models.CharField(max_length=150, verbose_name='Descripción')),
                ('turno', models.CharField(max_length=150, verbose_name='Turno')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'db_table': 'area',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('fullname', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=8, verbose_name='Dni')),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('gender', models.CharField(max_length=20, verbose_name='Sexo')),
                ('state_civil', models.CharField(max_length=50, verbose_name='Estado Civil')),
                ('date_birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(max_length=150, verbose_name='Dirección')),
                ('provincia', models.CharField(max_length=150, verbose_name='Provincia')),
                ('departamento', models.CharField(max_length=150, verbose_name='Departamento')),
                ('phone', models.CharField(max_length=7, verbose_name='Teléfono')),
                ('cellphone', models.CharField(max_length=9, verbose_name='Celular')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=8, verbose_name='Dni')),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('gender', models.CharField(max_length=20, verbose_name='Sexo')),
                ('address', models.CharField(max_length=150, verbose_name='Dirección')),
                ('cellphone', models.CharField(max_length=9, verbose_name='Celular')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('state', models.BooleanField(default=True)),
                ('date_entry', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de entrada')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.area')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empledos',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mz', models.CharField(max_length=3, verbose_name='Mz')),
                ('lote', models.PositiveSmallIntegerField()),
                ('state', models.BooleanField()),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('description', models.CharField(max_length=150, verbose_name='Descripción')),
                ('total_lote', models.IntegerField(verbose_name='Total de lotes')),
                ('address', models.CharField(max_length=150, verbose_name='Dirección')),
                ('provincia', models.CharField(max_length=150, verbose_name='Provincia')),
                ('departamento', models.CharField(max_length=150, verbose_name='Departamento')),
                ('distrito', models.CharField(max_length=150, verbose_name='Distrito')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'db_table': 'proyecto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.cliente')),
                ('lider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.empleado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.proyecto')),
            ],
            options={
                'verbose_name': 'Visita',
                'verbose_name_plural': 'Visitas',
                'db_table': 'visita',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Monto')),
                ('concepto', models.CharField(max_length=150, verbose_name='Concepto')),
                ('voucher', models.CharField(max_length=30, verbose_name='Nro Voucher')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d')),
                ('state', models.BooleanField(verbose_name=True)),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.cliente')),
                ('plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.plano')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.proyecto')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reserva',
                'db_table': 'reserva',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('type', models.CharField(max_length=150, verbose_name='Tipo de Puesto')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=9)),
                ('horario', models.CharField(max_length=150, verbose_name='Horario')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_uptated', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.area')),
            ],
            options={
                'verbose_name': 'Puesto',
                'verbose_name_plural': 'Puesto',
                'db_table': 'puesto',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='plano',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.proyecto'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.puesto'),
        ),
    ]
