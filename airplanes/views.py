from typing import List

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AirplaneSerializer
from .services import flight_time, fuel_capacity, fuel_consumption_per_min
from .utils import convert_decimal_to_min


class AirplaneCapacityView(APIView):

    @swagger_auto_schema(
        request_body=AirplaneSerializer(many=True),
        operation_description="Endpoint to calculate fuel consumption per minute and airplane flight time for multiple airplanes.",
        responses={200: "Success"},
    )
    def post(self, request: Request) -> Response:
        """
        POST method to calculate fuel consumption per minute and airplane flight time for multiple airplanes.

        Params:
            request (Request): The incoming request containing data for multiple airplanes.

        Returns:
            Response: JSON response containing fuel consumption per minute and airplane flight time for each airplane.
        """
        serializer = AirplaneSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            airplanes_data: List[dict] = serializer.validated_data
            response_data: List[dict] = []
            for data in airplanes_data:
                consumption_per_min = fuel_consumption_per_min(
                    airplane_id=data.get("id"),
                    no_of_passengers=data.get("passengers")
                )
                airplane_flight_time = flight_time(
                    total_fuel=fuel_capacity(airplane_id=data.get("id")),
                    consumption_per_min=consumption_per_min,
                )
                response_data.append(
                    {
                        "id": data.get("id"),
                        "fuel_consumption_per_min": f"{consumption_per_min} litre/minute",
                        "airplane_flight_time": f"{convert_decimal_to_min(airplane_flight_time)} minutes",
                    }
                )
            return Response(response_data, status=status.HTTP_200_OK)
