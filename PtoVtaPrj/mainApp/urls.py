from django.urls import path
from . import views
from VtasApp.views import VentasView, ClientesView, EquiposView, createSaleView, saleListView
from InvApp.views import ProveedoresView, MaterialesView, ProductosView
from InvApp.views import inventory_list, inventory_create, inventory_update


urlpatterns = [
    path('', views.mainView, name='mainView'),
    path('informes/', views.informesView, name='informesView'),
    path('dashboard/', views.dashboardView, name='dashboardView'),
    path('vtas/', VentasView, name='VtaView'),
    path('clis/', ClientesView, name='CliView'),
    path('eqs/', EquiposView, name='EqView'),
    # path('inv/', InventariosView, name='InvView'),
    path('prov/', ProveedoresView, name='ProvView'),
    path('mat/', MaterialesView, name='MatView'),
    path('prod/', ProductosView, name='ProdView'),

    path('create/', createSaleView, name='csaleView'),
    path('list/', saleListView, name='slistView'),

    path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/create/', inventory_create, name='inventory_create'),
    path('inventory/update/<int:pk>/', inventory_update, name='inventory_update'),

]
