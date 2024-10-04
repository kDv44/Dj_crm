import os

from datetime import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from dotenv import load_dotenv, dotenv_values

load_dotenv()


class Customer(models.Model):

    name = models.TextField(verbose_name="Company name")
    email = models.EmailField(verbose_name="Email", null=False, blank=True)
    phone = PhoneNumberField(
        region=str(os.getenv("PHONE_ZONE")),
        verbose_name="Phone number",
        null=True,
        blank=False,
        default=None,
    )
    city = models.TextField(verbose_name="City")
    address = models.TextField(verbose_name="Address")

    class Meta:
        db_table = "Customers"
        verbose_name = "Description counterparty"
        verbose_name_plural = "Description counterparty"

    def __str__(self):
        return f"{self.name} / {self.address}"


class Device(models.Model):

    manufacturer = models.TextField(verbose_name="Manufacturer")
    model = models.TextField(verbose_name="Model")

    date_entered = models.DateTimeField(
        verbose_name="Date Entered", null=True, blank=True
    )
    date_returned = models.DateTimeField(
        verbose_name="Date Returned", null=True, blank=True
    )
    is_in_field = models.BooleanField(default=False, verbose_name="Is in Field")

    Customer.objects.select_related("device_in_field").all()

    class Meta:
        db_table = "Devices"
        verbose_name = "Available Devices"
        verbose_name_plural = "Available Devices"

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    def save(self, *args, **kwargs):
        if self.date_returned and self.date_returned < self.date_entered:
            raise ValueError("Date Returned cannot be earlier than Date Entered.")
        super().save(*args, **kwargs)


class DeviceInField(models.Model):

    serial_number = models.TextField(verbose_name="Serial number")
    customer = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, verbose_name="Customer"
    )
    field_device = models.ForeignKey(
        Device, blank=True, null=True, on_delete=models.RESTRICT, verbose_name="Device"
    )
    owner_status = models.TextField(verbose_name="Affiliation status")

    class Meta:
        db_table = "Devices_in_fields"
        verbose_name = "Devices in field"
        verbose_name_plural = "Devices in field"

    def __str__(self):
        return f"{self.field_device} serial number > {self.serial_number} in {self.customer}"


class Order(models.Model):

    STATUSES = (
        ("open", "Open"),
        ("closed", "Closed"),
        ("in progress", "In progress"),
        ("need info", "Need info"),
    )

    device = models.ForeignKey(Device, verbose_name="Device", on_delete=models.RESTRICT)
    order_description = models.TextField(verbose_name="Description")
    created_dt = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_updated_dt = models.DateTimeField(
        verbose_name="Last update", blank=True, null=True, default=datetime.now()
    )
    order_status = models.TextField(verbose_name="Order status", choices=STATUSES)

    class Meta:
        db_table = "Orders"
        verbose_name = "Orders"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order №{self.id} for {self.device}"
