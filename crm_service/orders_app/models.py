from datetime import datetime
from xml.dom import ValidationErr

from django.db import models
from django.utils.translation.trans_null import gettext_lazy


class Device(models.Model):

    class Meta:
        db_table = "Devices"
        verbose_name = "Available Devices"
        verbose_name_plural = "Available Devices"

    manufacturer = models.TextField(verbose_name="Manufacturer")
    model = models.TextField(verbose_name="Model")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Customer(models.Model):

    class Meta:
        db_table = "Customers"
        verbose_name = "Description counterparty"
        verbose_name_plural = "Description counterparty"

    customer_name = models.TextField(verbose_name="Company name")
    customer_city = models.TextField(verbose_name="City")
    customer_address = models.TextField(verbose_name="Address")

    def __str__(self):
        return self.customer_name


class DeviceInField(models.Model):

    class Meta:
        db_table = "Devices_in_fields"
        verbose_name = "Devices in field"
        verbose_name_plural = "Devices in field"

    serial_number = models.TextField(verbose_name="Serial number")
    customer_id = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, verbose_name="Customer id"
    )
    analyzer_id = models.ForeignKey(
        Device, on_delete=models.RESTRICT, verbose_name="Analyzer id"
    )
    owner_status = models.TextField(verbose_name="Affiliation status")


def status_validator(order_status):
    if order_status not in ["open", "closed", "in progress", "need info"]:
        raise ValidationErr(
            gettext_lazy("%(order_status)s is wrong order status"),
            params={"order status": order_status},
        )


class Order(models.Model):

    class Meta:
        db_table = "Orders"
        verbose_name = "Orders"
        verbose_name_plural = "Orders"

    devices = models.ForeignKey(
        Device, verbose_name="Device", on_delete=models.RESTRICT
    )
    customer = models.ForeignKey(
        Customer, verbose_name="End user", on_delete=models.RESTRICT
    )
    description = models.TextField(verbose_name="Description")
    created_dt = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update_dt = models.DateTimeField(
        verbose_name="Last update", blank=True, null=True
    )
    order_status = models.TextField(
        verbose_name="Order status", validators=[status_validator]
    )

    def save(self, *args, **kwargs):
        self.last_update_dt = datetime.now()
        super().save(*args, **kwargs)
