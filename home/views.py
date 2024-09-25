from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples=[
        {'name': 'saurabh','age': 22 },
        {'name': 'tushar','age': 21 },
        {'name': 'ajaya','age': 23 },
        {'name': 'ajit','age': 16 }
    ]
    
    
    
    return render(request, 'home/index.html',context={'peoples':peoples})

    
    
def success_page(request):
    return HttpResponse("<h1> hey this is my success page!</h1>")
    