from django.urls import path

from core.reports.views import ReportClienteView

urlpatterns = [
    # reports
    path('cliente/', ReportClienteView.as_view(), name='cliente_report'),
]
