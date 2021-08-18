from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Hello world</h1>')

def basic_load(request):
    return render(request, 'first.html', {'name':'navin'})

def basic_form(request):
    return render(request, 'second.html')

def add(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    c = a + b
    return render(request,'third.html',{'result':c})
