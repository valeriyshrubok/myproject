from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    position = models.CharField(max_length=200, verbose_name='Должность')
    employment_date = models.DateTimeField(verbose_name='Дата принятия на работу')
    salary = models.IntegerField(default=0, verbose_name='ЗП')
    lvl = models.CharField(max_length=50, verbose_name='Уровень')
    chief = models.ForeignKey('Chief', on_delete=models.PROTECT, verbose_name='Начальник')
    paid_salary = models.ForeignKey('Paid_salary', on_delete=models.CASCADE, verbose_name='Выплаченная зп')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'

class Chief(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Начальник'
        verbose_name_plural = 'Начальники'

class Paid_salary(models.Model):
    info = models.IntegerField(db_index=True, verbose_name='Выплаченная зп')

    class Meta:
        verbose_name = 'Выплаченная зарплата'
        verbose_name_plural = 'Выплаченные зарплаты'