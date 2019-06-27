from django.http import HttpResponse

def index(request):
    return HttpResponse("ITS MAIN DOMAIN!")