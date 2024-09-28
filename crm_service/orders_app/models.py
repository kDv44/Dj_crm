from datetime import datetime
from django.db import models


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
        return f"{self.customer_name} / {self.customer_address}"


class DeviceInField(models.Model):

    class Meta:
        db_table = "Devices_in_fields"
        verbose_name = "Devices in field"
        verbose_name_plural = "Devices in field"

    serial_number = models.TextField(verbose_name="Serial number")
    customer = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, verbose_name="Customer"
    )
    analyzer = models.ForeignKey(
        Device, on_delete=models.RESTRICT, verbose_name="Equipment"
    )
    owner_status = models.TextField(verbose_name="Affiliation status")

    def __str__(self):
        return (
            f"{self.analyzer} serial number > {self.serial_number} in {self.customer}"
        )


class Order(models.Model):

    class Meta:
        db_table = "Orders"
        verbose_name = "Orders"
        verbose_name_plural = "Orders"

    statuses = (
        ("open", "Open"),
        ("closed", "Closed"),
        ("in progress", "In progress"),
        ("need info", "Need info"),
    )

    device = models.ForeignKey(Device, verbose_name="Device", on_delete=models.RESTRICT)
    order_description = models.TextField(verbose_name="Description")
    created_dt = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_updated_dt = models.DateTimeField(
        verbose_name="Last update", blank=True, null=True
    )
    order_status = models.TextField(verbose_name="Order status", choices=statuses)

    def __str__(self):
        return f"Order №{self.id} for {self.device}"

    def save(self, *args, **kwargs):
        self.last_update_dt = datetime.now()
        super().save(*args, **kwargs)
