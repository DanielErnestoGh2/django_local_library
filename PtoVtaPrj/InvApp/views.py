#from django.shortcuts import render

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
#@login_required

#@permission_required('InvApp.view_producto', raise_exception=True)
#@permission_required('InvApp.change_producto', raise_exception=True)

# def InventariosView(request):
#     return render(request, 'Inventarios.html')

def ProveedoresView(request):
    return render(request, 'Proveedores.html')

def MaterialesView(request):
    return render(request, 'Materiales.html')

def ProductosView(request):
    return render(request, 'Productos.html')

from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
from .models import Company, UserProfile, Inventory
from .forms import InventoryForm

@login_required
def inventory_list(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    inventories = Inventory.objects.filter(company=user_profile.company)
    return render(request, 'inventorylist.html', {'inventories': inventories})

@login_required
def inventory_create(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.company = user_profile.company
            inventory.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'inventoryForm.html', {'form': form})

@login_required
def inventory_update(request, pk):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    inventory = get_object_or_404(Inventory, pk=pk, company=user_profile.company)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'inventoryForm.html', {'form': form})