from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
