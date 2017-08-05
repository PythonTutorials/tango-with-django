from django.shortcuts import render, get_object_or_404

from rango.models import Category, Page


def index(request):
    ctx_dict = {
        'categories': Category.objects.order_by('-likes')[:5],
        'pages': Page.objects.order_by('-views')[:5]
    }
    return render(request, 'rango/index.html', context=ctx_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    pages = Page.objects.filter(category=category)
    ctx_dict = {'category': category, 'pages': pages}

    return render(request, 'rango/category.html', context=ctx_dict)
