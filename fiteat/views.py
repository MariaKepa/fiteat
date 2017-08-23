# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Category
from .models import Product



# Create your views here.

def first_page(request):
    return render (request, 'fiteat/first_page.html', {})

    
def product(request):
    categorys = Category.objects.all()
    return render (request, 'fiteat/products.html', {'categorys':categorys})

def product_detail(request, id):
    product_list = Product.objects.filter(category__id=id)
    return render(request,'fiteat/product_detail.html', {'products':product_list})

def contact(request):
    return render(request, 'fiteat/nav_menu/contact.html', {})

def aboutme(request):
    return render(request, 'fiteat/nav_menu/aboutme.html', {})

def statute(request):
    return render(request, 'fiteat/nav_menu/statute.html', {})

def tips(request):
    return render(request, 'fiteat/nav_menu/tips.html', {})

def dairy(request):
    return render(request, 'fiteat/nav_menu/dairy.html', {})

def body_weight(request):
    return render(request, 'fiteat/nav_menu/body_weight.html', {})

def edit_panel(request):
    return render(request, 'fiteat/nav_menu/edit_panel.html', {})


# ----------REGISTRATION------

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'fiteat/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'fiteat/register.html', {'user_form':user_form})


# ---------------LOGIN---------
@login_required
def dashboard(request):
    return render(request, 'fiteat/dashboard.html', {})
