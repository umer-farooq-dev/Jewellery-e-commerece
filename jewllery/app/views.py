import requests
from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm, CusomerProfileForm
from django.contrib import messages
from .models import *


def home(request):
    return render(request, 'app/home.html')


class ProductView(View):
    def get(self, request):
        ring = Product.objects.filter(category='R')
        bracelet = Product.objects.filter(category='B')
        necklace = Product.objects.filter(category='N')
        return render(request, 'app/home.html', {'ring': ring, 'bracelet': bracelet, 'necklace': necklace})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def mobile(request):
    return render(request, 'app/mobile.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()

        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


def checkout(request):
    return render(request, 'app/checkout.html')


class ProfileView(View):
    def get(self, request):
        form = CusomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CusomerProfileForm(requests.post)
        if form.is_valid():
            usr = request.user
            name = form.changed_data['name']
            locality = form.changed_data['locality']
            city = form.changed_data['city']
            zipcode = form.changed_data['zipcode']
            reg = Customer(user=usr, name=name, Locality=locality, city=city, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
            return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
