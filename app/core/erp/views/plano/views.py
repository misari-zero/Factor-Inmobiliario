from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import PlanoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Plano


class PlanoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Plano
    template_name = 'plano/list.html'
    permission_required = 'erp.view_plano'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Plano.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Planos'
        context['create_url'] = reverse_lazy('erp:plano_create')
        context['list_url'] = reverse_lazy('erp:plano_list')
        context['entity'] = 'Planos'
        return context


class PlanoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Plano
    form_class = PlanoForm
    template_name = 'plano/create.html'
    success_url = reverse_lazy('erp:plano_list')
    permission_required = 'erp.add_plano'
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
        context['title'] = 'Creación de Plano'
        context['entity'] = 'Planos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class PlanoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Plano
    form_class = PlanoForm
    template_name = 'plano/create.html'
    success_url = reverse_lazy('erp:plano_list')
    permission_required = 'erp.change_plano'
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
        context['title'] = 'Edición de Plano'
        context['entity'] = 'Planos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class PlanoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Plano
    template_name = 'plano/delete.html'
    success_url = reverse_lazy('erp:plano_list')
    permission_required = 'erp.delete_plano'
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
        context['title'] = 'Eliminación de Plano'
        context['entity'] = 'Planos'
        context['list_url'] = self.success_url
        return context
