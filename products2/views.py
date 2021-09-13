from django.shortcuts import render
from products2.models import Product, ProductTest
from .forms import RawProductForm
from .forms import ProductForm
# Create your views here.


def products_detail_views(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
    }
    return render(request, 'products/detail.html', context)


def prod_det_views(request):
    obj = ProductTest.objects.get(id=1)
    context = {
        'title': obj.title,
        'price': obj.price
    }
    return render(request, 'products/det.html', context)

'''
def products_create_views(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/products_create.html', context)
'''


def products_create_views(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, 'products/products_create.html', context)