import pytest

from crm_service.orders_app.models import Customer


@pytest.mark.django_db
def test_create_customer():
    customer_data = {
        "customer_name": "Test Company",
        "customer_email": "test@example.com",
        "customer_phone": "+00000000000",
        "customer_city": "Test City",
        "customer_address": "Test Address",
    }
    customer = Customer(**customer_data)
    customer.save()
    assert Customer.objects.count() == 1
    assert Customer.objects.get().customer_name == "Test Company"
