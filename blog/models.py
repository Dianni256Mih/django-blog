from django.db import models

# Create your models here.

class Post(models.Model):
  body_text = models.TextField('Texto Principal')
  pub_date = models.DateTimeField('Data Publicação', auto_now=True)
