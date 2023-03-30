# Stdlib Imports
import uuid

from django.db import models
from django.db.models import Index

class Company(models.Model):
    """
    Defines the schema for Assets_comapny table in the database.

    Fields:
        - id (int): the object unique uuid
        - name (str): the name of country
    """

    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=100)

class Device(models.Model):
    """
    Defines the schema for Assets_comapny table in the database.

    Fields:
        - id (int): the object unique uuid
        - name (str): the name of the device
        - company (Fk): Foreign Key to the company who issued the device
        - condition (str): Choice field for the condition of the device
    """
    
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)

class Employee(models.Model):
    """
    Defines the schema for Assets_comapny table in the database.

    Fields:
        - id (int): the object unique uuid
        - name (str): the name of the employee
        - company (Fk): Foreign Key to the company the employee works at
        - issued_devices (m2m): many to many relationship to the Devices table to know how many devices have been issued to this employee
    """
    
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    issued_devices = models.ManyToManyField(Device, through='Checkout')

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
    
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    condition_out = models.CharField(max_length=100)
    condition_in = models.CharField(max_length=100, null=True, blank=True)
    