from django.urls import path
from . import views

urlpatterns = [
    path('new', views.create_city),
    path('', views.list_cities),
]