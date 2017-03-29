from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, User

from django.views.generic import TemplateView # Import TemplateView

# Create your views here.

def users_view(request):
    users = User.objects.all()
    return render(request, 'user.html', {'users': users})

def products_view(request):
    all_products = Product.objects.all()
    html = ''
    for products in all_products:
        url = '/product/' + str(products.id) + '/'
        html +=  '<a href="' + url + '">' + products.name + '</a><br>'
    return HttpResponse(html)

