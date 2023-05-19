from django.urls import include, path

urlpatterns = [
    path('cities/', include('cities.urls'))
]