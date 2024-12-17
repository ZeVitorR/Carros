from django.shortcuts import render, redirect
from .models import Car
from .forms import CarModelForm
from django.views import View

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

class CarsView(View):

    def get(self, request):
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
    
def new_cars_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )

class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )
   
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )