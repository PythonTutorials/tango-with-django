from django.http import HttpResponse


def index(request):
    return HttpResponse(
        '<a href="/rango/about/">About</a>'
        '<h1>Rango says hey there partner!</h1>'
    )


def about(request):
    return HttpResponse(
        '<a href="/rango/">Index</a>'
        '<h1>Rango says here is the about page.</h1>'
    )
