from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add', views.Add_city.as_view(), name='add'),
    path('success', views.success, name='success'),
    path('get_cities', views.get_cities, name='get_cities'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('about/<int:pk>', views.About.as_view(), name='about')
]