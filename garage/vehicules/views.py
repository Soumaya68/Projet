from django.shortcuts import render, redirect
from .models import Vehicule
from .forms import VehiculeForm

def index(request):
    vehicules = Vehicule.objects.all()
    return render(request, 'vehicules/index.html', {'vehicules': vehicules})

def ajouter_vehicule(request):
    if request.method == 'POST':
        form = VehiculeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculeForm()
    return render(request, 'vehicules/ajouter.html', {'form': form})
