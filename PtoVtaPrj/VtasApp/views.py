from django.shortcuts import render, redirect

#Para que no se pueda acceder sin login (login_required) y para controlar los accesos a los modelos (permission_required)
from django.contrib.auth.decorators import login_required, permission_required

from .models import Product, Sale, SaleItem
from .forms import SaleForm, SaleItemForm


# Create your views here.

@login_required
# Permisos en los MODELOS App.view_model, App.add_model, App.change_model, App.delete_model

#@permission_required('VtasApp.view_venta', raise_exception=True)
#@permission_required('VtasApp.change_venta', raise_exception=True)

def VentasView(request):
    return render(request, 'Ventas.html')

def ClientesView(request):
    return render(request, 'Clientes.html')

def EquiposView(request):
    return render(request, 'Equipos.html')


def createSaleView(request):
    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        if sale_form.is_valid():
            sale = sale_form.save(commit=False)
            sale.total = 0
            sale.save()
            for product_id, quantity in request.POST.getlist('products'):
                product = Product.objects.get(id=product_id)
                price = product.price * int(quantity)
                sale_item = SaleItem(sale=sale, product=product, quantity=quantity, price=price)
                sale_item.save()
                sale.total += price
            sale.save()
            return redirect('slistView')
    else:
        sale_form = SaleForm()
    return render(request, 'createSale.html', {'sale_form': sale_form})

def saleListView(request):
    sales = Sale.objects.all()
    return render(request, 'saleList.html', {'sales': sales})