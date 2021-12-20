from django.shortcuts import render
from .models import Car
from .filters import CarFilter

# Create your views here.
def index(request):
    new_cars = Car.objects.filter(category='New')[:8]
    used_cars = Car.objects.filter(category='Used')[:8]
    latest_cars = Car.objects.all().order_by('-date')[:5]
    all=Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=all)
    all=myFilter.qs

    context = {
        'new_cars':new_cars,
        'used_cars':used_cars,
        'latest_cars':latest_cars,
        'all':all,
        'myFilter':myFilter

    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def filter_results(request):
    all=Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=all)
    all=myFilter.qs

    context={
        'all':all,
        'myFilter':myFilter
    }
    return render(request, 'filter_results.html', context)
