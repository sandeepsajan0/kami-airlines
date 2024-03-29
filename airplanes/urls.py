from django.urls import path

from .views import AirplaneCapacityView


urlpatterns = [
    path('capacity/', AirplaneCapacityView.as_view(), name="airplanes_consumption_and_fly_time"),
]