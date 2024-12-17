from django.shortcuts import render, redirect
from .models import Car
from .forms import CarModelForm
from django.views import View
from django.views.generic import ListView

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

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if (search):
            cars = cars.filter(model__icontains=search)
        return cars

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