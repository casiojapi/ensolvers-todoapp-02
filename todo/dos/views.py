from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    dos = Do.objects.all()

    context = {'dos': dos}
    return render(request, 'dos/index.html', context)