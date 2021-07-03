from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    dos = Do.objects.all()

    form = DoForm()

    if request.method == 'POST':
        form = DoForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('/')

    context = {'dos': dos, 'form': form}

    return render(request, 'dos/index.html', context)