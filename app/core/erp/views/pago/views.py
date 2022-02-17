from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import PagoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Pago


class PagoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Pago
    template_name = 'pago/list.html'
    permission_required = 'erp.view_pago'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Pago.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pagos'
        context['create_url'] = reverse_lazy('erp:pago_create')
        context['list_url'] = reverse_lazy('erp:pago_list')
        context['entity'] = 'Pagos'
        return context


class PagoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pago/create.html'
    success_url = reverse_lazy('erp:pago_list')
    permission_required = 'erp.add_pago'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Pago'
        context['entity'] = 'Pagos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class PagoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pago/create.html'
    success_url = reverse_lazy('erp:pago_list')
    permission_required = 'erp.change_pago'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Pago'
        context['entity'] = 'Pagos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class PagoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Pago
    template_name = 'pago/delete.html'
    success_url = reverse_lazy('erp:pago_list')
    permission_required = 'erp.delete_pago'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Pago'
        context['entity'] = 'Pagos'
        context['list_url'] = self.success_url
        return context
