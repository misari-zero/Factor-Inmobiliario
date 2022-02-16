from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import AgendaForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Agenda, Empleado


class AgendaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Agenda
    template_name = 'agenda/list.html'
    permission_required = 'erp.view_agenda'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Agenda.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Agenda'
        context['create_url'] = reverse_lazy('erp:agenda_create')
        context['list_url'] = reverse_lazy('erp:agenda_list')
        context['entity'] = 'Agendas'
        return context


class AgendaCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Agenda
    form_class = AgendaForm
    # queryset = Empleado.objects.filter(puesto='')
    template_name = 'agenda/create.html'
    success_url = reverse_lazy('erp:agenda_list')
    permission_required = 'erp.add_agenda'
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
        context['title'] = 'Creación un Agenda'
        context['entity'] = 'Agendas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class AgendaUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agenda/create.html'
    success_url = reverse_lazy('erp:agenda_list')
    permission_required = 'erp.change_agenda'
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
        context['title'] = 'Edición de Agenda'
        context['entity'] = 'Agendas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class AgendaDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Agenda
    template_name = 'agenda/delete.html'
    success_url = reverse_lazy('erp:agenda_list')
    permission_required = 'erp.delete_agenda'
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
        context['title'] = 'Eliminación de Agenda'
        context['entity'] = 'Agendas'
        context['list_url'] = self.success_url
        return context
