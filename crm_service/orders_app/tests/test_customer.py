import pytest

from unittest.mock import patch
from orders_app.models import Customer


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


@patch("orders_app.views.Customer.objects.all")
def test_get_customers(mock_get_all):
    mock_get_all.return_value = [
        Customer(customer_name="Mock Company", customer_email="mock@example.com")
    ]

    # Здесь вы можете вызвать вашу вьюху и проверить результат
    response = ...  # Используйте ваш механизм для тестирования вьюх
    assert response.status_code == 200
    assert len(response.data) == 1
