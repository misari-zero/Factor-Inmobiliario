from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import InventarioForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Inventario


class InventarioListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Inventario
    template_name = 'inventario/list.html'
    permission_required = 'erp.view_inventario'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Inventario.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Inventario'
        context['create_url'] = reverse_lazy('erp:inventario_create')
        context['list_url'] = reverse_lazy('erp:inventario_list')
        context['entity'] = 'Inventarios'
        return context


class InventarioCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/create.html'
    success_url = reverse_lazy('erp:inventario_list')
    permission_required = 'erp.add_inventario'
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
        context['title'] = 'Creación de Inventario'
        context['entity'] = 'Inventario'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class InventarioUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/create.html'
    success_url = reverse_lazy('erp:inventario_list')
    permission_required = 'erp.change_inventario'
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
        context['title'] = 'Edición un Inventario'
        context['entity'] = 'Inventarios'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class InventarioDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Inventario
    template_name = 'inventario/delete.html'
    success_url = reverse_lazy('erp:inventario_list')
    permission_required = 'erp.delete_inventario'
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
        context['title'] = 'Eliminación de Inventario'
        context['entity'] = 'Inventarios'
        context['list_url'] = self.success_url
        return context
