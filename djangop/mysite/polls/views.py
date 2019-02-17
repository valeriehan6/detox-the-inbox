from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, welcome to Detox the Inbox!")