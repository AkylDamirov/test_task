from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from .models import Cities
from .forms import CitiesForm, NearestForm


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
    form = NearestForm
    return render(request, 'task_app/nearest.html', {'form':form})



























