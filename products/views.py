from django.shortcuts import render
from django.http import JsonResponse
from products.models import *
from .forms import *

# Create your views here.

def get_all_products(request):
    # get all products from the database
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def get_product(request, id):
    # get a single product from the database
    product = None
    try:
      product = Product.objects.get(id=id)
      return render(request, 'products/product.html', {'product': product})
    except Product.DoesNotExist:
        return render(request, 'not-found.html')

def create_product(request):
    # if the request is a POST request, then we need to create a new product
    if request.method == 'POST':
        # get the data from the request
        name = request.POST.get('name')
        description = request.POST.get('description')
        supplier_price = request.POST.get('supplier_price')
        selling_price = request.POST.get('selling_price')
        stock = request.POST.get('stock')
        image_url = request.POST.get('image_url')

        # create a new product
        product = Product(name=name, description=description, supplier_price=supplier_price, selling_price=selling_price, stock=stock, image_url=image_url)
        product.save()

        # redirect to the product page
        return render(request, 'products/product.html', {'product': product})
    else:
        # if the request is a GET request, then we need to return the form
        form = ProductForm()
        return render(request, 'products/create-product.html', {'form': form})