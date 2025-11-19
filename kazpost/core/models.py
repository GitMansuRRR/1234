from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name

class OperatorWindow(models.Model):
    window_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department.name}-{self.window_number}"

class QueueTicket(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'В ожидании'),
        ('called', 'Вызван'), 
        ('done', 'Обслужен'),
    ]

    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name='Услуга')
    ticket_number = models.CharField(max_length=10, verbose_name='Номер талона')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

