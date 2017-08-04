from django.shortcuts import render

from rango.models import Category


def index(request):
    ctx_dict = {'categories': Category.objects.order_by('-likes')[:5]}
    return render(request, 'rango/index.html', context=ctx_dict)


def about(request):
    return render(request, 'rango/about.html')
