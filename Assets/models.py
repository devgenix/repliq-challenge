# Stdlib Imports
import uuid

# Django imports
from django.db import models
from django.db.models import Index
from django.contrib.auth import get_user_model

User = get_user_model()

class Device(models.Model):
    """
    Defines the schema for Assets_comapny table in the database.

    Fields:
        - id (int): the object unique uuid
        - name (str): the name of the device
        - company (Fk): Foreign Key to the company who issued the device
        - condition (str): Choice field for the condition of the device
    """

    CHOICES = (
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Normal", "Normal"),
        ("Bad", "Bad"),
    )

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE,
        related_name='device_company'
    )

    name = models.CharField(
        max_length=100
    )

    condition = models.CharField(
        max_length=100,
        choices=CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_checked_out = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Devices"
        indexes = [
            Index(fields=[
                'name',
                'id'
            ]),
        ]

    def __str__(self) -> str:
        return self.name + " owned by " + self.company.name + " in condition: " + self.condition

class Checkout(models.Model):
    """
    Defines the schema for Assets_comapny table in the database.

    Fields:
        - id (int): the object unique uuid
        - employee (Fk): Foreign Key to the employee who checked out the device
        - device (Fk): Foreign Key to the device that was checked out
        - checkout_date (Datetime): The date and time when the device was checked out
        - return_date (Datetime): The date and time when the device was returned
        - condition_out (str): Choice field for the condition of the device when it was checked out
        - condition_in (str): Choice field for the condition of the device when it was returned
    """

    CHOICES = (
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Normal", "Normal"),
        ("Bad", "Bad"),
    )

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )

    checkout_date = models.DateTimeField(
        auto_now_add=True
    )

    return_date = models.DateTimeField(
        null=True,
        blank=True
    )

    condition_out = models.CharField(
        max_length=100,
        choices=CHOICES
    )

    condition_in = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=CHOICES
    )

    class Meta:
        verbose_name_plural = "Checkouts"
        indexes = [
            Index(fields=[
                'id'
            ]),
        ]

    def __str__(self) -> str:
        return self.device + " checked out by " + self.employee + " on " + self.checkout_date + " and returned on " + self.return_date + " in condition: " + self.condition_in

class Company(models.Model):
    """
    Defines the schema for Assets_comapny table in the database.

    Fields:
        - id (int): the object unique uuid
        - name (str): the name of country
    """

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    name = models.CharField(
        max_length=100
    )

    employees = models.ManyToManyField(
        User,
        related_name='company_employees',
        editable=False
    )

    devices = models.ManyToManyField(
        Device,
        related_name='company_devices',
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        verbose_name_plural = "Companies"
        indexes = [
            Index(fields=[
                'name',
                'id'
            ]),
        ]

    def __str__(self) -> str:
        return self.name + " with total employees: " + str(self.employees.count()) + " and total devices: " + str(self.devices.count())
