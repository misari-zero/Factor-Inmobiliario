from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ContabilidadForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Contabilidad


class ContabilidadListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Contabilidad
    template_name = 'contabilidad/list.html'
    permission_required = 'erp.view_contabilidad'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Contabilidad.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Contabilidad'
        context['create_url'] = reverse_lazy('erp:contabilidad_create')
        context['list_url'] = reverse_lazy('erp:contabilidad_list')
        context['entity'] = 'Contabilidad'
        return context


class ContabilidadCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Contabilidad
    form_class = ContabilidadForm
    template_name = 'contabilidad/create.html'
    success_url = reverse_lazy('erp:contabilidad_list')
    permission_required = 'erp.add_contabilidad'
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
        context['title'] = 'Creación de Contabilidad'
        context['entity'] = 'Contabilidad'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ContabilidadUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Contabilidad
    form_class = ContabilidadForm
    template_name = 'contabilidad/create.html'
    success_url = reverse_lazy('erp:contabilidad_list')
    permission_required = 'erp.change_contabilidad'
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
        context['title'] = 'Edición de Contabilidad'
        context['entity'] = 'Contabilidad'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ContabilidadDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Contabilidad
    template_name = 'contabilidad/delete.html'
    success_url = reverse_lazy('erp:contabilidad_list')
    permission_required = 'erp.delete_contabilidad'
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
        context['title'] = 'Eliminación de un Contabilidad'
        context['entity'] = 'Contabilidad'
        context['list_url'] = self.success_url
        return context
