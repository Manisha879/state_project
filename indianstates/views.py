from django.shortcuts import render,HttpResponse, redirect

# Create your views here.


from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import IndianState


def create(request):
    if request.method=='POST':
        #print("request is:",request.method)
        n=request.POST['uname']
        cap=request.POST['ucapital']
        p=request.POST['pop']
        l=request.POST['lang']
        m=IndianState.objects.create(name=n,capital=cap,population=p,language=l)
        m.save()
        #print(n,"-",cap,"-",p,"-",l,"-")
        #return HttpResponse ("data instertted sucessfully")
        return redirect('/dashboard')
    else:
       return render(request,'create.html')    


def dashboard(request):
    m=IndianState.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    #return HttpResponse ("data fetched")


def delete(request,rid):
    #print("id to be deleted",rid)
    m=IndianState.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')
    #return HttpResponse("idto be deleted:"+rid)

def edit(request,rid):
   # print("id to be edite:",rid)
   if request.method=='POST':
         n=request.POST['uname']
         cap=request.POST['ucapital']
         p=request.POST['pop']
         l=request.POST['lang']
        # print(n)
         #return HttpResponse("update")
         m=IndianState.objects.filter(id=rid)
         m.update(name=n,capital=cap,population=p,language=l)
         return redirect('/dashboard')
   else:
     m=IndianState.objects.get(id=rid)
     context={}
     context['data']=m
     return render(request,'edit.html',context)      
     #return HttpResponse("id to be edited",+rid)    