from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer


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
