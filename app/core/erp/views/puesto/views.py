from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import PuestoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Puesto


class PuestoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Puesto
    template_name = 'puesto/list.html'
    permission_required = 'erp.view_puesto'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Puesto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Puesto'
        context['create_url'] = reverse_lazy('erp:puesto_create')
        context['list_url'] = reverse_lazy('erp:puesto_list')
        context['entity'] = 'Puestos'
        return context


class PuestoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'puesto/create.html'
    success_url = reverse_lazy('erp:puesto_list')
    permission_required = 'erp.add_puesto'
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
        context['title'] = 'Creación un Puesto'
        context['entity'] = 'Puesto'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class PuestoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'Puesto/create.html'
    success_url = reverse_lazy('erp:puesto_list')
    permission_required = 'erp.change_puesto'
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
        context['title'] = 'Edición de Puesto'
        context['entity'] = 'Puestos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class PuestoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Puesto
    template_name = 'puesto/delete.html'
    success_url = reverse_lazy('erp:puesto_list')
    permission_required = 'erp.delete_puesto'
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
        context['title'] = 'Eliminación de un Puesto'
        context['entity'] = 'Puestos'
        context['list_url'] = self.success_url
        return context
