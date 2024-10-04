from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Device, Customer
from .serializers import CustomerSerializer, DeviceSerializer
from rest_framework import filters


class DeviceListCreate(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ["manufacturer", "model"]
    search_fields = ["manufacturer", "model"]


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ["city", "email"]
    search_fields = ["city", "email"]


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
