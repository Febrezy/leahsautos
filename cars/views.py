from django.shortcuts import render
from .models import Cars

def home(request):
    return render(request, 'cars/home.html')


def cars(request):
    cars = Cars.objects.all()
    return render(request,'cars/cars.html', {'cars': cars})
