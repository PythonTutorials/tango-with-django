from django.shortcuts import render


def index(request):
    ctx_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=ctx_dict)


def about(request):
    return render(request, 'rango/about.html')
