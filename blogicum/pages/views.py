from django.shortcuts import render


def about(request):
    """Функция обрабатывает ссылку о проекте."""
    template_about = 'pages/about.html'
    return render(request, template_about)


def rules(request):
    """Функция обрабатывает ссылку о правилах блога."""
    template_rules = 'pages/rules.html'
    return render(request, template_rules)
