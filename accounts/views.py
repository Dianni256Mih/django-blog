from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password # para criptografar a senha
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model() # obtém o model padrão para usuários do Django
from accounts.forms import AccountSignupForm # importa o form de registro
class AccountCreateView(CreateView):
  model = User # conecta o model a view
  template_name = 'registration/signup_form.html' # template para o form HTML
  form_class = AccountSignupForm # conecta o form a view
  success_url = reverse_lazy('login') # destino após a criação do novo usuário
  success_message = 'Usuário criado com sucesso!'
def form_valid(self, form): # executa quando os dados estiverem válidos
  form.instance.password = make_password(form.instance.password)
  form.save()
  messages.success(self.request, self.success_message)
  return super(AccountCreateView, self).form_valid(form)

