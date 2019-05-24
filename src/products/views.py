from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm
from products.forms import RawProductForm
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def product_detail_view(request, my_id):
    try:
        obj = Product.objects.get(id=my_id);

        context = {
            'title': obj.title
        }
        return render(request, "products/product.html", context)
    except:
        pass

    return HttpResponseNotFound("not found");

def product_list_view(request):
    objects = Product.objects.all()

    context = {
        'list': objects
    }

    return render(request, "products/product_list.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id);

    if request.method == "POST":
        obj.delete();
        return redirect('/')

    return render(request, "products/product_delete.html", {})

def product_create_view_old(request):
    initial_data = {
        'title': 'Initial value'
    }
    form = RawProductForm(request.POST or None, initial=initial_data)

    if form.is_valid():
        print(form.cleaned_data)
        Product.objects.create(**form.cleaned_data);
    else:
        print(form.errors)

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_create_view(request):

    initial_data = {
        'title': 'Initial value'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data,instance=obj)

    print(form.is_valid())
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)