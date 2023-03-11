from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Persona

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Personas(request):
    P = list(Persona.objects.values())
    return JsonResponse(P, safe=False)