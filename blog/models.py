from django.db import models

# Create your models here.

class Post(models.Model):
  body_text = models.TextField('Texto Principal')
  pub_date = models.DateTimeField('Data Publicação')
  categoria = models.CharField(
  'Categoria',
  max_length=15,
  choices=[
    ('noticias', 'Notícias'),
    ('como_fazer', 'Como Fazer'),
    ('review', 'Review'),
  ],
  default=None,
  null=True
)

