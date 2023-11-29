from django.shortcuts import render,redirect
from .models import Product, Commande,Newsletter,Contact

# Create your views here.

def index(request):
     product_object = Product.objects.all()
     if request.method == "POST":
          new_email = request.POST.get('new_email')
          comz = Newsletter(new_email = new_email)
          comz.save()
     search=request.GET.get('search')
     if search != '' and search is not None:
          product_object=Product.objects.filter(title__icontains=search)
     return render(request, 'shop/index.html',{'product_object':product_object})

def detail(request, myid):
     product_objecte = Product.objects.all()
     product_object = Product.objects.get(id=myid)
     if request.method == "POST":
          new_email = request.POST.get('new_email')
          comz = Newsletter(new_email = new_email)
          comz.save()
          return redirect('home')
     return render(request, 'shop/detail.html',{'product':product_object,'product_object':product_objecte})

def contact(request):
     if request.method == "POST":
          nom = request.POST.get('nom')
          email = request.POST.get('email')
          besoin = request.POST.get('besoin')
          message = request.POST.get('message')
          con = Contact( nom=nom, email=email, message=message, besoin=besoin)           
          con.save()
          return redirect('home')
     if request.method == "POST":
          new_email = request.POST.get('new_email')
          comz = Newsletter(new_email = new_email)
          comz.save()
          return redirect('home')
     return render(request, 'shop/contact.html')

def checkout(request):
     if request.method == "POST":
          items =request.POST.get('items')
          total =request.POST.get('total')
          nom = request.POST.get('nom')
          email = request.POST.get('email')
          address = request.POST.get('address')
          ville = request.POST.get('ville')
          pays = request.POST.get('pays')
          num = request.POST.get('num')
          com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, num=num)           
          com.save()
          return redirect('confirmation')
     return render(request, 'shop/checkout.html')

def confirmation(request):
     info = Commande.objects.all()[:1]
     for item in info:
          nom= item.nom
          num= item.num
     return render(request, 'shop/confirmation.html',{'name':nom,'num':num})

def boutique(request):
     product_object = Product.objects.all()
     search=request.GET.get('search')
     if search != '' and search is not None:
          product_object=Product.objects.filter(title__icontains=search)
     if request.method == "POST":
          new_email = request.POST.get('new_email')
          comz = Newsletter(new_email = new_email)
          comz.save()
          return redirect('home')
     return render(request, 'shop/product.html',{'product_object':product_object})

def apropos(request):
     if request.method == "POST":
          new_email = request.POST.get('new_email')
          comz = Newsletter(new_email = new_email)
          comz.save()
          return redirect('home')
     return render(request, "shop/apropos.html")
