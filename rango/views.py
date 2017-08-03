from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    ctx_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=ctx_dict)


def about(request):
    return HttpResponse(
        '<a href="/rango/">Index</a>'
        '<h1>Rango says here is the about page.</h1>'
    )
