from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return render(request,'rohit.html')
    
def boom(request):
    return HttpResponse('<h1>best bolwer in current time</h1')