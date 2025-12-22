from django.shortcuts import render, redirect
from .models import Product,Category,Comment
from django.views import View
from django.shortcuts import get_object_or_404
from .forms import ProductForms, CommentForm
from django.db.models import Q


class Home(View):
    def get(self, request):
        q = request.GET.get('q')
        if q:
            products = Product.objects.filter(
                Q(name__icontains=q) | Q(price__icontains=q) | Q(metal__icontains=q)
            )
            if len(products) == 0:
                products = Product.objects.all().order_by('-id')
        else:
            products = Product.objects.all().order_by('-id')

        categories = Category.objects.all()

        return render(request,
            template_name='list_products.html',
            context={'products': products,
            'categories': categories}
        )


class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        comments=product.comments.all().order_by('-id')
        context = {'product': product,'comments':comments}
        return render(request, 'detail.html', context)



class CategoryDetail(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        products = Product.objects.filter(category=category).order_by('-id')
        context = {
            'category': category,
            'products': products
        }
        return render(request, 'Category_detail.html', context)


class ProductCreate(View):
    def get(self, request):
        form = ProductForms()
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'form': form, 'categories': categories})

    def post(self, request):
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.owner=request.user
            product.save()
            return redirect('home')
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'form': form, 'categories': categories})



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

class CreateCommentView(View):
    def post(self,request,pk):
        product=get_object_or_404(Product,pk=pk)
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            coment=form.save(commit=False)
            coment.product=product
            coment.user=request.user
            coment.save()
        return redirect('detail',pk=product.pk)


class CommentUpdate(View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(instance=comment)
        return render(request, 'comment_edit.html', {
            'form': form,
            'comment': comment
        })

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(request.POST, request.FILES, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('detail', pk=comment.product.pk)

        return render(request, 'comment_edit.html', {
            'form': form,
            'comment': comment
        })

class CommentDelete(View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk, user=request.user)
        product_pk = comment.product.pk
        comment.delete()
        return redirect('detail', pk=product_pk)


