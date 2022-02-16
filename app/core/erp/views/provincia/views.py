from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ProvinciaForm
from core.erp.models import Provincia


class ProvinciaListView(ListView):
    model = Provincia
    template_name = 'provincia/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Provincia.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Provincia'
        context['create_url'] = reverse_lazy('erp:provincia_create')
        context['list_url'] = reverse_lazy('erp:provincia_list')
        context['entity'] = 'Provincias'
        return context


class ProvinciaCreateView(CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'provincia/create.html'
    success_url = reverse_lazy('erp:provincia_list')

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
        context['title'] = 'Creación de Provincia'
        context['entity'] = 'Provincias'
        context['list_url'] = reverse_lazy('erp:provincia_list')
        context['action'] = 'add'
        return context


class ProvinciaUpdateView(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'provincia/create.html'
    success_url = reverse_lazy('erp:provincia_list')

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
        context['title'] = 'Edición de Provincia'
        context['entity'] = 'Provincias'
        context['list_url'] = reverse_lazy('erp:provincia_list')
        context['action'] = 'edit'
        return context


class ProvinciaDeleteView(DeleteView):
    model = Provincia
    template_name = 'provincia/delete.html'
    success_url = reverse_lazy('erp:provincia_list')

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
        context['title'] = 'Eliminación de Provincia'
        context['entity'] = 'Provincias'
        context['list_url'] = reverse_lazy('erp:provincia_list')

        return context
