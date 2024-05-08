from datetime import datetime
from blog.models import Post, Category
from django.shortcuts import render, get_object_or_404


def index(request):
    """Функция обрабатывает ссылку на Главную страницу index.html."""
    max_count_publish_posts = 5
    template_index = 'blog/index.html'
    index_data = Post.objects.select_related(
        'category'
    ).filter(
        pub_date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-id')[0:max_count_publish_posts]

    context = {'post_list': index_data}
    return render(request, template_index, context)


def post_detail(request, post_id):
    """Функция обрабатывает ссылку на Отдельный пост."""
    template_detail = 'blog/detail.html'
    post_detail = get_object_or_404(
        Post.objects.all().filter(
            pub_date__lte=datetime.now(),
            is_published=True,
            category__is_published=True
        ),
        pk=post_id
    )
    context = {'post': post_detail}
    return render(request, template_detail, context)


def category_posts(request, category_slug):
    """Функция обрабатывает ссылку на раздел Категории."""
    template_category = 'blog/category.html'

    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )

    post_list = Post.objects.select_related(
        'category'
    ).filter(
        is_published=True,
        category__slug=category_slug,
        pub_date__lte=datetime.now()
    )

    context = {'post_list': post_list,
               'category': category}
    return render(request, template_category, context)
