from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm
from products.forms import RawProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1);
    context = {
        'title': obj.title
    }
    return render(request, "products/product.html", context)

def product_create_view(request):
    form = RawProductForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        Product.objects.create(**form.cleaned_data);
    else:
        print(form.errors)

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_create_view_old(request):
    form = ProductForm(request.POST or None)
    obj = Product.objects.get(id=1);

    print(form.is_valid())
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)