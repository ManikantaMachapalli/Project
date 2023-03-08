from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mani(request):
    return HttpResponse('How to create a multi apps in django')
