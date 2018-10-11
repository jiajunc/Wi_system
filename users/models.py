# users/models.py
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):

    is_doctor = models.BooleanField('Doctor', default=False)
    is_patient = models.BooleanField('Patient', default=False)

    def __str__(self):
        return self.username