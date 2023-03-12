from django.shortcuts import render,get_object_or_404

from django.contrib.gis.geoip2 import GeoIP2

from .models import Category,Product
from cart.forms import CartAddProductForm



# def getting_loc(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     g = GeoIP2()
#     location = g.city(ip)
#     location_city = location["city"]
#     return location_city


def product_list(request,category_slug=None):
    # city=getting_loc(request)
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True,store__city_name='Nuzvid')
    
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products})

# Create your views here.
def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form=CartAddProductForm()
    return render(request,'shop/product/detail.html',{'product':product,'cart_product_form':cart_product_form})

