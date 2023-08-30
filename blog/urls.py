from django.urls import path
from blog.views import index, ola, post_show, PostDetailView

urlpatterns = [
    path('index/', index, name= "index"),
    path('ola/', ola, name= "ola"),
    path('posts/all', ola, name="posts_list"),
    path('post/<int:post_id>', post_show, name="exibe_post"),
    path('post/<int:pk>/show', PostDetailView.as_view(), name="post_detail"),
]