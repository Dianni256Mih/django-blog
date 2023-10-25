from django.urls import path
from blog.views import (index, ola, post_show, PostDetailView, get_all_posts, get_post, PostCreateView, create_post, PostListView, SobreTemplateView, PostUpdateView, PostDeleteView,
)

urlpatterns = [
    path('', index, name= "index"),
    path('index/', index, name= "index"),
    path('ola/', ola, name= "ola"),
    path('posts/all', ola, name="posts_list"),
    path('post/<int:post_id>', post_show, name="exibe_post"),
    path('post/<int:pk>/show', PostDetailView.as_view(), name="post_detail"),
    path('api/posts', get_all_posts, name="posts_data"),
    path('api/posts/<int:post_id>', get_post, name="post_data"),
    path('post/add', PostCreateView.as_view(), name="post_add"),
    path('api/post/add', create_post, name="create_post_data"),
    path('posts', PostListView.as_view(), name="posts_all"),
    path('about-us', SobreTemplateView.as_view(), name="about_page"),
    path('account/<int:pk>/edit', views.AccountUpdateView.as_view(), name="account_edit"),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post_delete"),
]
