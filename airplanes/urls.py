from django.urls import path

from .views import AirplaneView


urlpatterns = [
    path('capacity/', AirplaneView.as_view(), name="airplanes_consumption_and_fly_time"),
]