from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from orders_app.views import (
    DeviceListCreate,
    DeviceDetail,
    CustomerListCreate,
    CustomerDetail,
)

import debug_toolbar


schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version="v1",
        description="My API description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    ### swager ###
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ### debug toolbar URLS ###
    path("__debug__/", include(debug_toolbar.urls)),
    ### device ###
    path("api/device/", DeviceListCreate.as_view(), name="device-list-create"),
    path("api/device/<int:pk>/", DeviceDetail.as_view(), name="device-detail"),
    ### customer ###
    path("api/customers/", CustomerListCreate.as_view(), name="customer-list-create"),
    path("api/customers/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
]
