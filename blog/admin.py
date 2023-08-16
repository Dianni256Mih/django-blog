# importa o decorator admin que habilita características de admin no nosso model
from django.contrib import admin
from blog.models import Post # importa o model que vamos habilitar no admin site
@admin.register(Post) # registar o model Post e habilita
class PostAdmin(admin.ModelAdmin): # configura o model Post no admin site.
  list_display = ('id', 'body_text', 'pub_date')
  list_filter = ('pub_date',)