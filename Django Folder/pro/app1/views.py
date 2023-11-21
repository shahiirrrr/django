from django.shortcuts import render
from app1.models import *
from app1.form import*

# Create your views here.
def home(request):
    d=student.objects.all()
    return render(request,'home.html',{'data':d})

def index(request):
    return render(request,'index.html')

def form1(request):
    form=studentform()
    if(request.method =='POST'):
        form=studentform(request.POST)
        if (form.is_valid()):
            form.save()
            return home (request)
    return render(request,'form1.html',{'form':form})
            
        
def form2(request):
    
    if(request.method =='POST'):
        form=studentform(request.POST)
        if (form.is_valid()):
            form.save()
            return home (request)
    return render(request,'form2.html')
