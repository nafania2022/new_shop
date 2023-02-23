from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *
from .utils import *
from .form import *
# Create your views here.

class Home(DataMixin, ListView):
    model = Products
    template_name = 'online_shop/home.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Главная страница')
        return dict(list(context.items())+ list(con.items()))

class ProductShow(DataMixin, DetailView):
    model = Products
    slug_url_kwarg = 'slug_product'
    template_name = 'online_shop/show_product.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title=context['products'])
        return dict(list(context.items())+ list(con.items()))


class CategoryShow(DataMixin, ListView):
    model = Products
    slug_url_kwarg = 'slug_cat'
    template_name = 'online_shop/show_category.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['slug_cat'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title=context['products'][0].category)
        return dict(list(context.items())+ list(con.items()))


class AddProduct(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'online_shop/add_product.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Добавить товар')
        return dict(list(context.items())+ list(con.items()))
    