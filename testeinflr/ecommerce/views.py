from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

from django.views.generic import TemplateView # Import TemplateView

# Create your views here.
def home(request):
    context = locals()
    template = 'index.html'
    return render(request, template, context)

def products_view(request):
    all_products = Product.objects.all()
    html = ''
    template = 'products_view.html'
    for products in all_products:
        url = '/product/' + str(products.id) + '/'
        html +=  '<a href="' + url + '">' + products.name + '</a><br>'
    return HttpResponse(html)



