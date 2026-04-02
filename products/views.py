from django.views.generic import ListView, DetailView
from .models import Category, Product

class ProductListView(ListView):
    model = Category
    template_name = 'products/list.html'
    context_object_name = 'categories'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
