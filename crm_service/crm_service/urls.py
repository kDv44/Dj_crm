"""
URL configuration for crm_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from orders_app.views import (
    CustomerListCreate,
    CustomerDetail,
    CustomerByCity,
    CustomerByEmail,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/customers/", CustomerListCreate.as_view(), name="customer-list-create"),
    path("api/customers/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
    path(
        "api/customers/city/<str:city>/",
        CustomerByCity.as_view(),
        name="customer-by-city",
    ),
    path(
        "api/customers/email/<str:email>/",
        CustomerByEmail.as_view(),
        name="customer-by-email",
    ),
]
