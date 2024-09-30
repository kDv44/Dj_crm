from rest_framework import serializers
from .models import Customer


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
