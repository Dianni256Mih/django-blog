import os
from uuid import uuid4
def safe_rename(instance, filename): # função para renomear o arquivo de forma segura
  extension = filename.split('.')[-1]
  filename = f'{uuid4().hex}.{extension}'
  return os.path.join('images', filename)

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser): # herda o model User base padrão do Django
  data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
  cpf = models.CharField("CPF", max_length=11, null=True, blank=True)
  imagem = models.FileField(
    upload_to=safe_rename,
    default=None,
    null=True
)

