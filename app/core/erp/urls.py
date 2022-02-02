from django.urls import path

from core.erp.views.area.views import *

app_name = 'erp'

urlpatterns = [
    path('area/list/', AreaListView.as_view(), name='area_list'),
    path('area/add/', AreaCreateView.as_view(), name='area_create'),
    path('area/update/<int:pk>/', AreaUpdateView.as_view(), name='area_update'),
    path('area/delete/<int:pk>/', AreaDeleteView.as_view(), name='area_delete'),
]
