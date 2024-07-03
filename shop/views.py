from shop.forms import ProductForm
from shop.models import Category


# Create your views here.


def product_list(request):
    searched = request.GET.get('searched')
    if searched:
        products_list = Product.objects.filter(name__icontains=searched)
    else:
        products_list = Product.objects.all()

    categories_list = Category.objects.all()

    context = {'products_list': products_list,
               'categories_list': categories_list}

    return render(request, 'shop/home.html', context)


from django.shortcuts import render, redirect
from .models import Product, Comment, Order
from .forms import CommentForm, OrderForm


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    comments = Comment.objects.filter(product=product_id)
    orders = Order.objects.filter(product=product_id)

    if request.method == 'POST':
        if 'submit_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            order_form = OrderForm()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.product = product
                new_comment.save()
                return redirect('detail', product_id=product.id)
        elif 'submit_order' in request.POST:
            order_form = OrderForm(request.POST)
            comment_form = CommentForm()
            if order_form.is_valid():
                new_order = order_form.save(commit=False)
                new_order.product = product
                new_order.save()
                return redirect('detail', product_id=product.id)
    else:
        comment_form = CommentForm()
        order_form = OrderForm()

    context = {
        'product': product,
        'comments': comments,
        'orders': orders,
        'comment_form': comment_form,
        'order_form': order_form,
    }

    return render(request, 'shop/detail.html', context)


def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'shop/add-product.html', context)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(instance=product, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'shop/edit-product.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('home')


def login(request):
    return render(request, 'shop/login.html')


def register(request):
    return render(request, 'shop/register.html')


def categories(request):
    categories_list = Category.objects.all()
    context = {'categories_list': categories_list}
    return render(request, 'shop/base.html', context)


def products_of_category(request, category_id):
    products_category = Product.objects.filter(category_id=category_id)
    categories_list = Category.objects.all()

    context = {
        'products_list': products_category,
        'categories_list': categories_list,
    }

    return render(request, 'shop/home.html', context)
