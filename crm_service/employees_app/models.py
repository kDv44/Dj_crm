from django.db import models
from orders_app.models import Device, Customer


class Employer(models.Model):
    name = models.TextField(verbose_name="Employer name")
    email = models.EmailField(verbose_name="Email", null=False, blank=True)
    login = models.TextField(verbose_name="Login")
    password = models.TextField(verbose_name="Password")

    class Meta:
        db_table = "Employer"

    def __str__(self):
        return f"{self.name} / {self.email}"


class Activity(models.Model):
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, related_name="activities"
    )
    activity_type = models.CharField(max_length=100, verbose_name="Type of Activity")
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField(verbose_name="Start Time")
    end_time = models.DateTimeField(verbose_name="End Time", null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[("in_progress", "In Progress"), ("completed", "Completed")],
        default="in_progress",
    )

    class Meta:
        db_table = "Activity"

    def __str__(self):
        return f"{self.employer.name} - {self.activity_type} ({self.start_time} - {self.end_time})"
