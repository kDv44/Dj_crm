# Generated by Django 5.1.1 on 2024-10-09 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("orders_app", "0006_rename_name_customer_company_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(verbose_name="Employer name")),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="Email"),
                ),
                ("login", models.TextField(verbose_name="Login")),
                ("password", models.TextField(verbose_name="Password")),
            ],
            options={
                "db_table": "Employer",
            },
        ),
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "activity_type",
                    models.CharField(max_length=100, verbose_name="Type of Activity"),
                ),
                ("start_time", models.DateTimeField(verbose_name="Start Time")),
                (
                    "end_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="End Time"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "In Progress"),
                            ("completed", "Completed"),
                        ],
                        default="in_progress",
                        max_length=50,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="orders_app.customer",
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="orders_app.device",
                    ),
                ),
                (
                    "employer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="activities",
                        to="employees_app.employer",
                    ),
                ),
            ],
            options={
                "db_table": "Activity",
            },
        ),
    ]
