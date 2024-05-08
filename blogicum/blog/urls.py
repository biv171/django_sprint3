from django.urls import path

from .views import index, post_detail, category_posts

# Общее простраство имен
app_name = 'blog'

# Пути/ссылки приложения blog
urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', category_posts,
         name='category_posts'),
]
