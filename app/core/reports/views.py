from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.erp.models import Cliente
from core.reports.forms import ReportForm

from django.db.models.functions import Coalesce
from django.db.models import Sum


class ReportClienteView(TemplateView):
    template_name = 'cliente/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Cliente.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.names,
                        s.distrito.name,
                        s.provincia.name,
                        s.departamento.name,
                        s.date_joined.strftime('%Y-%m-%d'),
                    ])
                # data.append([
                #     '---',
                #     '---',
                #     '---',
                #     format(subtotal, '.2f'),
                #     format(iva, '.2f'),
                #     format(total, '.2f'),
                # ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Clientes'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('cliente_report')
        context['form'] = ReportForm()
        return context
