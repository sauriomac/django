from django.shortcuts import render

from product.models import Product

# Create your views here.
def basepage(request):
    return render(request, 'base.html')


def frontpage(request):
    New_Products = Product.objects.all()[0:8]

    return render(request, 'frontpage.html', {'New_Products': New_Products})