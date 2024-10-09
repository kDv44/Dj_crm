from django.contrib import admin

from .models import Order, Device, Customer, DeviceInField


class DeviceAdmin(admin.ModelAdmin):
    search_fields = ("manufacturer", "model")
    list_display = ("id", "manufacturer", "model")


class OrderAdmin(admin.ModelAdmin):

    def my_customer(self, obj):
        return obj.device.customer.name

    def my_serial_number(self, obj):
        return obj.device.number

    def my_device_model(self, obj):
        return obj.device.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.device.analyzer.manufacturer

    my_customer.short_description = "Customer"
    my_serial_number.short_description = "Serial number"
    my_device_model.short_description = "Model"
    my_device_manufacturer.short_description = "Manufacturer"

    list_display = (
        "id",
        "my_device_manufacturer",
        "my_device_model",
        "my_serial_number",
        "my_customer",
        "order_description",
        "created_dt",
        "last_updated_dt",
        "order_status",
    )
    search_fields = (
        "device__customer__customer_name",
        "device__id",
        "device__serial_number",
        "field_device__model",
        "field_device__manufacturer",
    )

    raw_id_fields = ("device",)


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ("company_name", "address")
    list_display = ("id", "company_name", "address", "city")


class DeviceInFieldAdmin(admin.ModelAdmin):
    def my_customer(self, obj):
        return obj.customer.customer_name

    def my_device_model(self, obj):
        return obj.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.analyzer.manufacturer

    my_customer.short_description = "Customer"
    my_device_manufacturer.short_description = "Manufacturer"
    my_device_model.short_description = "Model"

    list_display = ("serial_number", "customer", "field_device", "owner_status")
    search_fields = ("serial_number", "customer__name")
    list_filter = ("owner_status",)

    search_fields = ("serial_number",)
    raw_id_fields = ("customer", "field_device")
    list_display = (
        "id",
        "my_device_manufacturer",
        "my_device_model",
        "serial_number",
        "my_customer",
        "owner_status",
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
