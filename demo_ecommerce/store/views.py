from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from store import forms
from store.models import Product

def home(request):
    """READ: Display all products"""
    products = Product.objects.all()
    context_dict = {
        'products': products
    }
    return render(request, 'store.html', context_dict)


def add_product(request):
    """CREATE: Add a new product"""
    if request.method == 'POST':
        product_form = forms.ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
    else:
        product_form = forms.ProductForm()
    
    context_dict = {
        'product_form': product_form
    }
    return render(request, 'add_product.html', context_dict)


def edit_product(request, product_id):
    """UPDATE: Edit an existing product"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product_form = forms.ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
    else:
        product_form = forms.ProductForm(instance=product)
    
    context_dict = {
        'product_form': product_form,
        'product': product
    }
    return render(request, 'edit_product.html', context_dict)


def delete_product(request, product_id):
    """DELETE: Remove a product"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    context_dict = {
        'product': product
    }
    return render(request, 'delete_product.html', context_dict)

