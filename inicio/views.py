from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse('Hellow World')