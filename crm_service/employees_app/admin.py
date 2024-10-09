from django.contrib import admin

from .models import Employer, Activity


class EmployerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")


class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "employer",
        "activity_type",
        "customer",
        "device",
        "start_time",
        "end_time",
        "status",
    )
    search_fields = (
        "employer",
        "activity_type",
        "customer",
        "device",
        "start_time",
        "end_time",
        "status",
    )


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Activity, ActivityAdmin)
