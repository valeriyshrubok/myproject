from django.db import models
from django.db.models import Sum


class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    employment_date = models.DateTimeField(verbose_name='Дата принятия на работу')
    lvl = models.CharField(max_length=50, verbose_name='Уровень')
    position_id = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')
    chief_id = models.ForeignKey('Chief', on_delete=models.PROTECT, verbose_name='Начальник')
    salary_id = models.ForeignKey('Salary', on_delete=models.PROTECT, verbose_name='Зарплата')
    paid_salary_id = models.ForeignKey('Salary_info', null=True, on_delete=models.PROTECT, blank=True, verbose_name='Выплаченная зп')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Position(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название должности')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Salary(models.Model):
    salary = models.IntegerField(default=0, verbose_name='Зарплата')

    def __str__(self):
        return f'{str(self.salary)} $'

    class Meta:
        verbose_name = 'Зарплата'
        verbose_name_plural = 'Зарплаты'

class Salary_info(models.Model):
    paid_salary = models.IntegerField(default=0, verbose_name='Выплаченная зп')
    salary_info_id = models.ManyToManyField(Employee, null=True, blank=True)

    # sum = Employee.objects.filter(type='Flour').aggregate(Sum('paid_salary'))['paid_salary__sum']

    def __str__(self):
        return f'Выплаченная зп {self.paid_salary} $'


    class Meta:
        verbose_name = 'Выплаченная зарплата'
        verbose_name_plural = 'Выплаченные зарплаты'

class Chief(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя начальника')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Начальник'
        verbose_name_plural = 'Начальники'




