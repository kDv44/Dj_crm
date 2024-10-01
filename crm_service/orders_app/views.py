from rest_framework import generics
from .models import Device, Customer
from .serializers import CustomerSerializer, DeviceSerializer


### Device ###
class DeviceListCreate(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceByManufacturer(generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        manufacturer = self.kwargs["manufacturer"]
        return Customer.objects.filter(manufacturer=manufacturer)


class DeviceByModel(generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        model = self.kwargs["model"]
        return Customer.objects.filter(customer_email=model)


### Customer ###
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerByCity(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        city = self.kwargs["city"]
        return Customer.objects.filter(customer_city=city)


class CustomerByEmail(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        email = self.kwargs["email"]
        return Customer.objects.filter(customer_email=email)
