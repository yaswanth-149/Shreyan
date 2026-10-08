from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome shreyan it employees")

def about(request):
    return render(request, 'myapp/about.html')