from rest_framework import serializers
from .models import Device, Customer


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "manufacturer",
            "model",
        ]
        read_only_fields = ["id"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "phone",
            "city",
            "address",
        ]
        read_only_fields = ["id"]
