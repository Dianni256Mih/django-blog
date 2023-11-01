from django.db import models

from django.contrib.auth import get_user_model
user = get_user_model()

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
  
autor = models.ForeignKey(
  user, 
  editable = False,
  on_delete = models.DO_NOTHING,
  null = True
)



