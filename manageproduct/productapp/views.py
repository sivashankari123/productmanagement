from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request, "home.html")

def userdetails(request):
    products = Product.objects.all()  # fetch all products from database
    return render(request, "user.html", {'products': products})