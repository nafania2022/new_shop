from .models import *
from django.db.models import Count

menu = [
        {'title': "Добавить товар", 'url_name': 'add_prod'},

]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cat = Category.objects.annotate(Count('products'))
        
        context['cat'] = cat    
        context['menu'] = menu
        return context
        