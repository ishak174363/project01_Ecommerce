from django.shortcuts import render
# Import view
from django.views.generic import ListView,DetailView
# Import Model
from App_Shop.models import Product
# Import Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(ListView):
    model=Product
    template_name='App_Shop/home.html'

class ProductDetail(LoginRequiredMixin,DetailView):
    model=Product
    template_name='App_Shop/product_detail.html'