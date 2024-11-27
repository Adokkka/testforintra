from django.db import models
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True,       null=True)
    date = models.DateTimeField(null=True)
    objects = models.Manager()
    def __str__(self):
        return self.title


class DataItem(models.Model):
    name = models.CharField(max_length=255)
    namefull = models.CharField(max_length=255)
    rem = models.TextField(null=True, blank=True)
    uid = models.UUIDField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    uid = models.UUIDField()

    def __str__(self):
        return self.name




class Service(models.Model):
    nomenclatura_code = models.CharField(max_length=255, null=True, blank=True)
    nomenclatura_name = models.CharField(max_length=255)
    name = models.TextField()
    measure_name = models.CharField(max_length=255, null=True, blank=True)
    measure_code = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField()
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

class Matrix(models.Model):
    element_name = models.CharField(max_length=255)
    value_name = models.CharField(max_length=255)
    value_uid = models.CharField(max_length=255)

class Expenditure(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)
    nomer = models.CharField(max_length=255, blank=True, null=True)
    org_name = models.CharField(max_length=255)
    org_bin = models.CharField(max_length=255)
    datadoc = models.DateTimeField(null=True)
    autor_name = models.CharField(max_length=255)
    autor_iin = models.CharField(max_length=255)
    cost_name = models.CharField(max_length=255)
    cost_code = models.CharField(max_length=255)
    data_shipment = models.DateTimeField(null=True)
    Rem = models.TextField()
    Comment = models.TextField()
    TypeOfExpenditure = models.CharField(max_length=255)
    ReferenceDocument = models.TextField()
    SpecialRequirementsOfTheClient = models.TextField()
    services = models.ManyToManyField(Service)
    matrix = models.ManyToManyField(Matrix)
