from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser): # herda o model User base padrão do Django
  data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
  cpf = models.CharField("CPF", max_length=11, null=True, blank=True)

