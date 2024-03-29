from rest_framework import serializers


class AirplaneSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
    passengers = serializers.IntegerField(min_value=0)
