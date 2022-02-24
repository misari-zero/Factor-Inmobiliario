from django.urls import path

from core.erp.views.agenda.views import *
from core.erp.views.area.views import *
from core.erp.views.cliente.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.departamento.views import *
from core.erp.views.distrito.views import *
from core.erp.views.inventario.views import *
from core.erp.views.pago.views import *
from core.erp.views.plano.views import *
from core.erp.views.provincia.views import *
from core.erp.views.proyecto.views import *
from core.erp.views.puesto.views import *
from core.erp.views.empleado.views import *
from core.erp.views.reserva.views import *

app_name = 'erp'

urlpatterns = [
    # Area
    path('area/list/', AreaListView.as_view(), name='area_list'),
    path('area/add/', AreaCreateView.as_view(), name='area_create'),
    path('area/update/<int:pk>/', AreaUpdateView.as_view(), name='area_update'),
    path('area/delete/<int:pk>/', AreaDeleteView.as_view(), name='area_delete'),
    # Puesto
    path('puesto/list/', PuestoListView.as_view(), name='puesto_list'),
    path('puesto/add/', PuestoCreateView.as_view(), name='puesto_create'),
    path('puesto/update/<int:pk>/', PuestoUpdateView.as_view(), name='puesto_update'),
    path('puesto/delete/<int:pk>/', PuestoDeleteView.as_view(), name='puesto_delete'),
    # Departamento
    path('departamento/list/', DepartamentoListView.as_view(), name='departamento_list'),
    path('departamento/add/', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamento/update/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('departamento/delete/<int:pk>/', DepartamentoDeleteView.as_view(), name='departamento_delete'),
    # Provincia
    path('provincia/list/', ProvinciaListView.as_view(), name='provincia_list'),
    path('provincia/add/', ProvinciaCreateView.as_view(), name='provincia_create'),
    path('provincia/update/<int:pk>/', ProvinciaUpdateView.as_view(), name='provincia_update'),
    path('provincia/delete/<int:pk>/', ProvinciaDeleteView.as_view(), name='provincia_delete'),
    # Distrito
    path('distrito/list/', DistritoListView.as_view(), name='distrito_list'),
    path('distrito/add/', DistritoCreateView.as_view(), name='distrito_create'),
    path('distrito/update/<int:pk>/', DistritoUpdateView.as_view(), name='distrito_update'),
    path('distrito/delete/<int:pk>/', DistritoDeleteView.as_view(), name='distrito_delete'),
    # Empleado
    path('empleado/list/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleado/add/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleado/update/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleado/delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    # Cliente
    path('cliente/list/', ClienteListView.as_view(), name='cliente_list'),
    path('cliente/add/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
    # Proyecto
    path('proyecto/list/', ProyectoListView.as_view(), name='proyecto_list'),
    path('proyecto/add/', ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyecto/update/<int:pk>/', ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyecto/delete/<int:pk>/', ProyectoDeleteView.as_view(), name='proyecto_delete'),
    # Plano
    path('plano/list/', PlanoListView.as_view(), name='plano_list'),
    path('plano/add/', PlanoCreateView.as_view(), name='plano_create'),
    path('plano/update/<int:pk>/', PlanoUpdateView.as_view(), name='plano_update'),
    path('plano/delete/<int:pk>/', PlanoDeleteView.as_view(), name='plano_delete'),
    # Reserva
    path('reserva/list/', ReservaListView.as_view(), name='reserva_list'),
    path('reserva/add/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reserva/update/<int:pk>/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reserva_delete'),
    # Agenda
    path('agenda/list/', AgendaListView.as_view(), name='agenda_list'),
    path('agenda/add/', AgendaCreateView.as_view(), name='agenda_create'),
    path('agenda/update/<int:pk>/', AgendaUpdateView.as_view(), name='agenda_update'),
    path('agenda/delete/<int:pk>/', AgendaDeleteView.as_view(), name='agenda_delete'),
    # Pago
    path('pago/list/', PagoListView.as_view(), name='pago_list'),
    path('pago/add/', PagoCreateView.as_view(), name='pago_create'),
    path('pago/update/<int:pk>/', PagoUpdateView.as_view(), name='pago_update'),
    path('pago/delete/<int:pk>/', PagoDeleteView.as_view(), name='pago_delete'),
    # Inventario
    path('inventario/list/', InventarioListView.as_view(), name='inventario_list'),
    path('inventario/add/', InventarioCreateView.as_view(), name='inventario_create'),
    path('inventario/update/<int:pk>/', InventarioUpdateView.as_view(), name='inventario_update'),
    path('inventario/delete/<int:pk>/', InventarioDeleteView.as_view(), name='inventario_delete'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
