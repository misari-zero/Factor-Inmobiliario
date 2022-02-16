from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import DistritoForm
from core.erp.models import Distrito


class DistritoListView(ListView):
    model = Distrito
    template_name = 'distrito/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Distrito.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Distrito'
        context['create_url'] = reverse_lazy('erp:distrito_create')
        context['list_url'] = reverse_lazy('erp:distrito_list')
        context['entity'] = 'Distritos'
        return context


class DistritoCreateView(CreateView):
    model = Distrito
    form_class = DistritoForm
    template_name = 'distrito/create.html'
    success_url = reverse_lazy('erp:distrito_list')

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
        context['title'] = 'Creación de Distrito'
        context['entity'] = 'Distritos'
        context['list_url'] = reverse_lazy('erp:distrito_list')
        context['action'] = 'add'
        return context


class DistritoUpdateView(UpdateView):
    model = Distrito
    form_class = DistritoForm
    template_name = 'area/distrito.html'
    success_url = reverse_lazy('erp:distrito_list')

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
        context['title'] = 'Edición de Distrito'
        context['entity'] = 'Distritos'
        context['list_url'] = reverse_lazy('erp:distrito_list')
        context['action'] = 'edit'
        return context


class DistritoDeleteView(DeleteView):
    model = Distrito
    template_name = 'distrito/delete.html'
    success_url = reverse_lazy('erp:distrito_list')

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
        context['title'] = 'Eliminación de Distrito'
        context['entity'] = 'Distritos'
        context['list_url'] = reverse_lazy('erp:distrito_list')
        return context
