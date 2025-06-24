# Para el manejo del error 403

from django.shortcuts import render
from django.http import HttpResponseForbidden

def custom_403_view(request, exception=None):
    return render(request, '403.html', status=403)