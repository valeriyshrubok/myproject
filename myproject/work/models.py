from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    employment_date = models.DateTimeField('employment_date')
    salary = models.IntegerField
    lvl = models.CharField(max_length=50)
    chief = models.ForeignKey('Chief', on_delete=models.PROTECT)
    paid_salary = models.ForeignKey('Paid_salary', on_delete=models.CASCADE)

class Chief(models.Model):
    name = models.CharField(max_length=100, db_index=True)

class Paid_salary(models.Model):
    info = models.IntegerField(db_index=True)
