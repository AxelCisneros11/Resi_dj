# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    numerodetelefono = models.CharField(max_length=10, unique=True)
    division = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    agencia = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Cambiamos el related_name aquí
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Cambiamos el related_name aquí también
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
