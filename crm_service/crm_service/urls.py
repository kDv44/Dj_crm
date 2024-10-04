from django.contrib import admin
from django.urls import path

from orders_app.views import (
    DeviceListCreate,
    DeviceDetail,
    CustomerListCreate,
    CustomerDetail,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    ### device ###
    path("api/device/", DeviceListCreate.as_view(), name="device-list-create"),
    path("api/device/<int:pk>/", DeviceDetail.as_view(), name="device-detail"),
    ### customer ###
    path("api/customers/", CustomerListCreate.as_view(), name="customer-list-create"),
    path("api/customers/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
]
