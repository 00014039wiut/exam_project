from django.template import RequestContext

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


from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment, Order
from .forms import CommentForm, OrderForm


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    comments = Comment.objects.filter(product=product_id)
    orders = Order.objects.filter(product=product_id)
    category = product.category
    related_products = Product.objects.filter(category=category).exclude(id=product_id)

    context = {
        'product': product,
        'comments': comments,
        'orders': orders,
        'related_products': related_products,
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


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from shop.forms import LoginForm, RegisterModelForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'shop/login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('home')
    else:
        form = RegisterModelForm()

    return render(request, 'shop/register.html', {'form': form})


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


def add_comment(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.product = product
            comment.save()

            return redirect('detail', product_id)
    else:
        form = CommentForm(request.GET)

    return render(request, 'shop/detail.html', {'form': form, 'product': product})


def add_order(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.product = product
            new_order.save()
            return redirect('detail', product_id=product.id)
    else:
        order_form = OrderForm()

    return render(request, 'shop/detail.html', {'form': order_form, 'product': product})
