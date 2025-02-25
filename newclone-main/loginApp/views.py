from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST["EMAIL"]
        password = request.POST["PWD"]

        print(email + password)
        return render(request,'login.html')
    else: 
        return render(request,'login.html')

def register(request):
    return render(request,'register.html')