from django.shortcuts import render
from app1.models import *
from app1.form import*
# Create your views here.


def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def add(request):
    form=doctorform()
    if(request.method =='POST'):
        form=doctorform(request.POST)
        if (form.is_valid()):
            form.save()
            return view1(request)
    return render(request,'add.html',{'form':form})

def view1(request):
    d=doctor.objects.all()
    return render(request,'view1.html',{'data':d})
def edit(request,p):
    b=doctor.objects.get(pk=p)
    form=doctorform(instance=b)
    if(request.method =='POST'):
        form=doctorform(request.POST,instance=b)
        if (form.is_valid()):
            form.save()
            return view1(request)
    return render(request,'edit.html',{'form':form})
def delete_item(request,p):
    b=doctor.objects.get(pk=p)
    b.delete()
    return view1(request)
    
    