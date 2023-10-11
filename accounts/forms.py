from django import forms
from django.contrib.auth import get_user_model
User = get_user_model() # obtém o model padrão para usuários do Django
class AccountSignupForm(forms.ModelForm): # define um formulário para registro
  password = forms.CharField(label="Senha", max_length=50,
widget=forms.PasswordInput())
class Meta:
  model = User # conecta o form com o model padrão de usuário
  fields = ('username', 'email', 'data_nascimento', 'cpf' 'password', ) # campos do model a exibir
  widgets = { # data personalizada a nível de formulário para exibição
    'data_nascimento': forms.widgets.DateInput(
        attrs={'type': 'date', 'required': 'required'}
    ),
}
