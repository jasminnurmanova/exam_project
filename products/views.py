from django.shortcuts import render, redirect
from .models import Product,Category
from django.views import View
from django.shortcuts import get_object_or_404
from .forms import ProductForms
from django.db.models import Q


class Home(View):
    def get(self, request):
        query = request.GET.get('q', '')
        products = Product.objects.all().order_by('-id')  # базовый queryset

        if query:
            products = products.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        categories = Category.objects.all()  # для sidebar
        context = {
            'products': products,
            'categories': categories,
            'query': query
        }
        return render(request, 'list_products.html', context)

class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'detail.html', context)

class CategoryDetail(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        products = Product.objects.filter(category=category).order_by('-id')
        context = {
            'category': category,
            'products': products
        }
        return render(request, 'category_detail.html', context)


class ProductCreate(View):
    def get(self, request):
        form = ProductForms()
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'form': form, 'categories': categories})

    def post(self, request):
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'form': form, 'categories': categories})


from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForms
from .models import Product, Category

class ProductUpdate(View):
    def get(self, request):
        q = request.GET.get('q')
        if q:
            products = Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
            if len(products) == 0:
                products = Product.objects.all().order_by('-id')
        else:
            products = Product.objects.all().order_by('-id')
        return render(request, template_name='list_products.html', context={'products': products})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForms(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=product.pk)
        categories = Category.objects.all()
        return render(request, 'product_update.html', {'form': form, 'categories': categories, 'product': product})


class ProductUpdate(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForms(instance=product)
        categories = Category.objects.all()
        return render(request, 'product_update.html', {'form': form, 'categories': categories, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForms(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=product.pk)
        categories = Category.objects.all()
        return render(request, 'product_update.html', {'form': form, 'categories': categories, 'product': product})


class ProductDelete(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_delete.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('home')

