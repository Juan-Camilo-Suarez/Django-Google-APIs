from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("route", views.route, name="route"),
    path("map", views.map, name="map"),
]
