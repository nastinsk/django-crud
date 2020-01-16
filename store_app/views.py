from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductAddNew(CreateView):
    model = Product
    template_name = "product_new.html"
    fields = ['title', 'description', 'manufacturer']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product_update.html"
    fields = ['title', 'description', 'manufacturer']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy('home')