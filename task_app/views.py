from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from .models import Cities
from .forms import CitiesForm
from math import radians, sin, cos, sqrt, atan2
# Create your views here.

def main(request):
    return render(request, 'task_app/index.html')

class Add_city(CreateView):
    model = Cities
    form_class = CitiesForm
    template_name = 'task_app/add_city.html'
    success_url = 'success'

    def form_valid(self, form):
        return super().form_valid(form)

def success(request):
    return render(request, 'task_app/successful.html')

def get_cities(request):
    cities = Cities.objects.all()
    return render(request, 'task_app/cities.html', {'cities':cities[::-1]})

def delete(request, id):
    city = Cities.objects.get(id=id)
    city.delete()
    return render(request, 'task_app/successful.html')

class About(DetailView):
    model = Cities
    template_name = 'task_app/about.html'
    context_object_name = 'city'

def nearest(request):
    return render(request, 'task_app/nearest.html')

def find_nearest_cities(user_latitude, user_longitude):
    cities = Cities.objects.all()
    nearest_cities = []

    for city in cities:
        distance = calculate_distance(user_latitude, user_longitude, city.latitude, city.longitude)
        nearest_cities.append((city, distance))

    nearest_cities.sort(key=lambda x: x[1])
    return nearest_cities[:2]

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2-lat1)
    dlon = radians(lon2-lon1)
    a = sin(dlat/2)*sin(dlat/2)+cos(radians(lat1))*cos(radians((lat2)))*sin(dlon/2)*sin(dlon/2)
    c = 2*atan2(sqrt(a), sqrt(1-a))
    distance = R*c
    return distance

def nearest_cities_view(request):
    if request.method=='POST':
        user_latitude = float(request.POST.get('latitude'))
        user_longitude = float(request.POST.get('longitude'))
        nearest_cities = find_nearest_cities(user_latitude, user_longitude)
        return render(request, 'task_app/nearest2.html', {'nearest_cities':nearest_cities})
    else:
        return render(request, 'task_app/nearest.html')





































