from django.shortcuts import render
from django.contrib import messages
from ROApp.models.services import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

def service_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    # messages.success(request,f"Service '{service.title()}' viewed successfully.")
    return render(request, 'service_detail.html', {'service': service})
