from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorials

# Create your views here.

def homepage(request):
    return render(request, "main/home.html", {"tutorials":Tutorials.objects.all})
