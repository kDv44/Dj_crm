from django.contrib import admin
from django.urls import path, include

from orders_app.views import (
    DeviceListCreate,
    DeviceDetail,
    CustomerListCreate,
    CustomerDetail,
)

import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    ### debug toolbar URLS ###
    path("__debug__/", include(debug_toolbar.urls)),
    ### device ###
    path("api/device/", DeviceListCreate.as_view(), name="device-list-create"),
    path("api/device/<int:pk>/", DeviceDetail.as_view(), name="device-detail"),
    ### customer ###
    path("api/customers/", CustomerListCreate.as_view(), name="customer-list-create"),
    path("api/customers/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
]
