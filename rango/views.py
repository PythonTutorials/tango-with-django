from django.http import HttpResponse


def index(request):
    return HttpResponse('Rango syas hey there partner!')
