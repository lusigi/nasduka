from django.http import HttpResponse
from django.shortcuts import render

# we create functions here that are passed to the urls as second parameters 


def home(request):
    # return HttpResponse("Homepage")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')