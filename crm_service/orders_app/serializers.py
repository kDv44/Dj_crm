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
            "customer_name",
            "customer_email",
            "customer_phone",
            "customer_city",
            "customer_address",
        ]
        read_only_fields = ["id"]
