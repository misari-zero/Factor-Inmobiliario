from django.urls import path

from core.reports.views import *

urlpatterns = [
    # reports
    path('cliente/', ReportClienteView.as_view(), name='cliente_report'),
    # path('proyecto/', ReportProyectoView.as_view(), name='proyecto_report'),
]
