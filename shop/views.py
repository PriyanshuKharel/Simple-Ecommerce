from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from zmq import Context

from shop.models import Product,Contact
from math import ceil


# Create your views here.
def index(request):
    # objects=Product.objects.all()
    # context={
    #     'objects':objects 
    # }
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nslides=n//4+ceil((n/4)-(n//4))
    # params={'no of slides':nslides,'range':range(1,nslides),'product':products}
    # allProds=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    
    allProds=[]
    catprods=Product.objects.values('category','product_id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nslides),nslides])
    params={'allProds':allProds}
    return render(request,'index.html',params)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    
    return render(request,'contact.html')

def tracker(request):
    return render(request,'tracker.html')

def search(request):
    return render(request,'search.html')

def productView(request,myId):
    product=Product.objects.filter(product_id=myId)
    return render(request,'prodView.html',{'product':product[0]})

def checkout(request):
    return render(request,'checkout.html')



