from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from blog.forms import PostModelForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import json
from django.core.serializers.json import DjangoJSONEncoder

from django.views.generic.detail import DetailView

from django.shortcuts import render,  get_object_or_404, redirect

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# Incluir a classe httpresponse.
from django.http import HttpResponse

# Define uma function view chamada index.
@login_required # controle de acesso usando o decorador de função
def index(request):
#   return HttpResponse('Ola Django - index')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})# novo retorno

# Define uma function view chamada ola.
def ola(request):
    return render(request, 'home.html')

from blog.models import Post # Acrescentar
def ola(request): # Modificar
    # return HttpResponse('Olá django')
    posts = Post.objects.all() # recupera todos os posts do banco de dados
    context = {'posts_list': posts } # cria um dicionário com os dado
    return render(request, 'posts.html', context) # renderiza o template e passa o contexto
 
def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

def get_all_posts(request):
    posts = list(Post.objects.values('pk', 'body_text', 'pub_date'))
    data = {'success': True, 'posts': posts}
    json_data = json.dumps(data, indent=1, cls=DjangoJSONEncoder)
    response = HttpResponse(json_data, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    return response

def get_post(request, post_id):
    post = Post.objects.filter(
        pk=post_id
    ).values(
        'pk', 'body_text', 'pub_date'
    ).first()

    data = {'success': True, 'post': post}
    status = 200
    if post is None:
        data = {'success': False, 'error': 'Post ID não existe.'}
        status=404

    response = HttpResponse(
        json.dumps(data, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
        status=status
)
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    return response

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_form.html'
   # fields = ('body_text', )
    success_url = reverse_lazy('posts_all')
    form_class = PostModelForm
    success_message = 'Postagem salva com sucesso.'

def get_context_data(self, **kwargs):
    context = super(PostCreateView, self).get_context_data(**kwargs)
    context['form_title'] = 'Criando um post'
    return context

def form_valid(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super(PostCreateView, self).form_valid(request, *args, **kwargs)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        body_text = data.get('body_text')
        if body_text is None:
            data = {'success': False, 'error': 'Texto do post inválido.'}
            status = 400 # Bad Request => erro do client
        else:
            post = Post(body_text=body_text)
            post.save()
            post_data = Post.objects.filter(
                pk=post.id
              ).values(
                'pk', 'body_text', 'pub_date'
              ).first()
            data = {'success': True, 'post': post_data}
            status = 201 # Created
        response = HttpResponse(
            json.dumps(data, indent=1, cls=DjangoJSONEncoder),
            content_type="application/json",
            status=status
)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

class SobreTemplateView(TemplateView):
    template_name = 'post/sobre.html'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('posts_all')
    form_class = PostModelForm
    success_message = 'Postagem salva com sucesso.'

def get_context_data(self, **kwargs):
    context = super(PostUpdateView, self).get_context_data(**kwargs)
    context['form_title'] = 'Editando o post'
    return context


def form_valid(self, form):
    messages.success(self.request, self.success_message)
    return super(PostUpdateView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_confirm_delete_form.html'
    success_url = reverse_lazy('posts_all')
    success_message = 'A postagem foi excluída com sucesso.'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, self.success_message)
        return super(PostCreateView, self).form_valid(form)
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(PostCreateView, self).form_valid(form)
    
def post_send(request, post_id):
    post = get_object_or_404(Post, pk=post_id) 
    post_uri = reverse_lazy('post detail', args=[post_id])
    try:
        email = request. POST.get('email')
        if len(email) < 5:
            raise ValueError("E-mail inwalido")

        link = f'{request._current_scheme_host}{post_url}'
        template = 'post/post_send'
        text_message = render_to_string(f"{template}.txt", {'post_link': link})
        html_message = render_to_string(f" {template}.html", {'post_link': link})
        send_mail(
        subject = "Este assunto pode te interessari",
        message=text_message,
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list=[email],
        html_message = html_message,
        )

        messages.success(
             request, 'Postagen compartilhada com sucesso'
        )

    except ValueError as error: 
        messages.error(request, error)

    except:

        messages.error(
            request, 'Erro ao enviar a mensagem!'
        )

    return redirect(post_url)