from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"base.html")
def login(request):
    return render(request,"login.html")
def product(request):
    return render(request,"product.html")
def naruto(request):
    return render(request,"naruto.html")