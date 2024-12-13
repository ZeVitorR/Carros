from django.shortcuts import render
from .models import Car

# Create your views here.
def cars_view(request):
    search = request.GET.get('search')

    if (search):
        cars = Car.objects.filter(model__icontains=search)
    else:
        cars = Car.objects.all()

    cars = cars.order_by('model')

    return render(
        request,
        'cars.html',
        {'cars': cars})