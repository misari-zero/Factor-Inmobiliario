from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import AsistenciaForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Asistencia


class AsistenciaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Asistencia
    template_name = 'asistencia/list.html'
    permission_required = 'erp.view_asistencia'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Asistencia.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Asistencia'
        context['create_url'] = reverse_lazy('erp:asistencia_create')
        context['list_url'] = reverse_lazy('erp:asistencia_list')
        context['entity'] = 'Asistencias'
        return context


class AsistenciaCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'asistencia/create.html'
    success_url = reverse_lazy('erp:asistencia_list')
    permission_required = 'erp.add_asistencia'
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
        context['title'] = 'Creación de Asistencia'
        context['entity'] = 'Asistencias'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class AsistenciaUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'asistencia/create.html'
    success_url = reverse_lazy('erp:asistencia_list')
    permission_required = 'erp.change_asistencia'
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
        context['title'] = 'Edición de Asistencia'
        context['entity'] = 'Asistencias'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class AsistenciaDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Asistencia
    template_name = 'asistencia/delete.html'
    success_url = reverse_lazy('erp:asistencia_list')
    permission_required = 'erp.delete_asistencia'
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
        context['title'] = 'Eliminación de Asistencia'
        context['entity'] = 'Asistencias'
        context['list_url'] = self.success_url
        return context
