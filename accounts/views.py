from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class AccountUpdateView(LoginRequiredMixin, UpdateView):
  model = User
  template_name = 'accounts/user_form.html'
  fields = ('first_name', 'email', 'imagem', ) # incluir os campos que deseja liberar a edição
  success_url = reverse_lazy('posts_all') # rota para redirecionar após a edição
  success_message = 'Perfil atualizado com sucesso!'
 
  def get_queryset(self): # método que altera o objeto recuperado pela view
    user_id = self.kwargs.get('pk') # recupera o argumento vindo na URL / rota
    user = self.request.user # obtém o objeto usuário da sessão
    if user is None or not user.is_authenticated or user_id != user.id:
      return User.objects.none()

    return User.objects.filter(id=user.id) # apenas o usuário do perfil logado pode editar

def form_valid(self, form): # executa quando os dados estiverem válidos
  messages.success(self.request, self.success_message)
  return super(AccountUpdateView, self).form_valid(form)
