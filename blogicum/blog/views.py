from django.db.models.functions import Now
from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post

# основные данные по постам
POSTS = Post.objects.select_related(
    'category', 'location', 'author'
).filter(
    is_published=True,
    category__is_published=True,
    pub_date__lte=Now()
)
# кол-во постов выводимых на главную страницу
COUNT_OF_POSTS = 5


def index(request):
    """Функция обрабатывает ссылку на Главную страницу index.html."""
    template_index = 'blog/index.html'
    index_data = POSTS[:COUNT_OF_POSTS]
    context = {'post_list': index_data}
    return render(request, template_index, context)


def post_detail(request, post_id):
    """Функция обрабатывает ссылку на Отдельный пост."""
    template_detail = 'blog/detail.html'
    post_detail = get_object_or_404(POSTS, pk=post_id)
    context = {'post': post_detail}
    return render(request, template_detail, context)


def category_posts(request, category_slug):
    """Функция обрабатывает ссылку на раздел Категории."""
    template_category = 'blog/category.html'

    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )

    post_list = POSTS.filter(category__slug=category_slug)

    context = {'post_list': post_list,
               'category': category}
    return render(request, template_category, context)
