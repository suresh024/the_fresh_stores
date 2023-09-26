from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class CartView(View):
    template_name = 'cart/index.html'