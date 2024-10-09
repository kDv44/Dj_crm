from rest_framework import serializers
from .models import Device, Customer, DeviceInField


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "manufacturer",
            "model",
        ]
        read_only_fields = ["id"]


class DeviceInFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInField
        fields = [
            "serial_number",
            "customer",
            "field_device",
            "owner_status",
        ]

    def validate_owner_status(self, value):
        if value not in dict(DeviceInField.STATUS_CHOICES):
            raise serializers.ValidationError("Invalid status")
        return value


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
