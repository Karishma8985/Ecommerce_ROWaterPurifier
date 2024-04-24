from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from ROApp.models.customer import Customer
from django.views import  View
from ROApp.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)          # sqlite query for getting all product details.
        print(products)
        return render(request , 'cart.html' , {'products' : products} )




