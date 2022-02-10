from django.db import models
from datetime import datetime

# Create your models here.
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import gender_choices
from core.models import BaseModel


class Area(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    turno = models.CharField(max_length=150, verbose_name='Turno')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        db_table = 'area'
        ordering = ['id']


class Puesto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    type = models.CharField(max_length=150, verbose_name='Tipo de Puesto')
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Área')
    horario = models.CharField(max_length=150, verbose_name='Horario')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['salario'] = format(self.salario, '.2f')
        item['area'] = self.area.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'
        db_table = 'puesto'
        ordering = ['id']


class Departamento(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'departamento'
        ordering = ['id']


class Provincia(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        db_table = 'provincia'
        ordering = ['id']


class Distrito(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        db_table = 'distrito'
        ordering = ['id']


class Empleado(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=8, verbose_name='Dni', unique=True)
    age = models.PositiveSmallIntegerField(default=0)
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')
    address = models.CharField(max_length=150, verbose_name='Dirección')
    cellphone = models.CharField(max_length=9, verbose_name='Celular')
    email = models.EmailField(max_length=254, verbose_name='Correo')
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Área')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia')
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, verbose_name='Distrito')
    state = models.BooleanField(default=True)
    date_entry = models.DateField(default=datetime.now, verbose_name='Fecha de entrada')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']


class Cliente(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    fullname = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=8, verbose_name='Dni')
    age = models.PositiveSmallIntegerField(default=0)
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')
    state_civil = models.CharField(max_length=50, verbose_name='Estado Civil')
    date_birth = models.DateField(verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, verbose_name='Dirección')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia')
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, verbose_name='Distrito')
    phone = models.CharField(max_length=7, verbose_name='Teléfono')
    cellphone = models.CharField(max_length=9, verbose_name='Celular')
    email = models.EmailField(max_length=254, verbose_name='Correo')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['date_birth'] = self.date_joined.strftime('%Y-%m-%d')
        item['departamento'] = self.departamento.toJSON()
        item['provincia'] = self.provincia.toJSON()
        item['distrito'] = self.distrito.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']


class Proyecto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=150, verbose_name='Descripción')
    total_lote = models.IntegerField(verbose_name='Total de lotes')
    address = models.CharField(max_length=150, verbose_name='Dirección')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia')
    distrito = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Distrito')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['departamento'] = self.departamento.toJSON()
        item['provincia'] = self.provincia.toJSON()
        item['distrito'] = self.distrito.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        db_table = 'proyecto'
        ordering = ['id']


class Plano(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    mz = models.CharField(max_length=3, verbose_name='Mz')
    lote = models.PositiveSmallIntegerField()
    state = models.BooleanField()
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.proyecto

    def toJSON(self):
        item = model_to_dict(self)
        item['proyecto'] = self.proyecto.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        db_table = 'plano'
        ordering = ['id']


class Visita(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.proyecto

    def toJSON(self):
        item = model_to_dict(self)
        item['proyecto'] = self.proyecto.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        db_table = 'visita'
        ordering = ['id']


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Monto')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=150, verbose_name='Concepto')
    voucher = models.CharField(max_length=30, verbose_name='Nro Voucher')
    img = models.ImageField(upload_to='img/%Y/%m/%d', null=True, blank=True)
    state = models.BooleanField(True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente

    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['proyecto'] = self.proyecto.toJSON()
        item['plano'] = self.plano.toJSON()
        item['img'] = self.get_image()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reserva'
        db_table = 'reserva'
        ordering = ['id']
