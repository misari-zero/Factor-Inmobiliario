from django.urls import path

from core.erp.views.area.views import *
from core.erp.views.puesto.views import *
from core.erp.views.empleado.views import *

app_name = 'erp'

urlpatterns = [
    # Area
    path('area/list/', AreaListView.as_view(), name='area_list'),
    path('area/add/', AreaCreateView.as_view(), name='area_create'),
    path('area/update/<int:pk>/', AreaUpdateView.as_view(), name='area_update'),
    path('area/delete/<int:pk>/', AreaDeleteView.as_view(), name='area_delete'),
    # Puesto
    path('puesto/list/', PuestoListView.as_view(), name='area_list'),
    path('puesto/add/', PuestoCreateView.as_view(), name='area_create'),
    path('puesto/update/<int:pk>/', PuestoUpdateView.as_view(), name='area_update'),
    path('puesto/delete/<int:pk>/', PuestoDeleteView.as_view(), name='area_delete'),
    # Empleado
    path('empleado/list/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleado/add/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleado/update/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleado/delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
]
