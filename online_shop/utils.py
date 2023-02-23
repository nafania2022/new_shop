from .models import *
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

menu = [
        {'title': "О нас", 'url_name': 'home'},
        {'title': "Добавить товар", 'url_name': 'product_add'}
]

class DataMixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs
        cat = Category.objects.annotate(Count('products'))
        new_menu = menu.copy()
        if not self.request.user.is_authenticated:
            new_menu.pop(1)
        
        context['cat'] = cat    
        context['menu'] = new_menu
        return context
        