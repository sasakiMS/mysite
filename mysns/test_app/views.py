from django.http import HttpResponse

def index(requuest):
    return HttpResponse("Hello, world. You're at the polls index")
    