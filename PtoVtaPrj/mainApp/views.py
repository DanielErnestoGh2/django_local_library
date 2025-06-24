from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required

# Create your views here.

def mainView(request):
    return render(request, 'mainFrm.html')

def informesView(request):
    return render(request, 'infFrm.html')

def dashboardView(request):
    return render(request, 'dashboardFrm.html')
