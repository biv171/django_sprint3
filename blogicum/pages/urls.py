from django.urls import path

from .views import about, rules

# Общее простраство имен
app_name = 'pages'

# Пути/ссылки приложения blog
urlpatterns = [
    path('about/', about, name='about'),
    path('rules/', rules, name='rules'),
]
