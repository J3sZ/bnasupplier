from django.shortcuts import render
from django.http import HttpResponse
from .models import project

# Create your views here.

def index(request):
    projects = project.objects.all()
    return render(request, 'index.html', {
        'projects' : project
    })
        
def repuestos(request):
    return render (request, '')