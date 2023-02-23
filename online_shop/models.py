from django.db import models 
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)    
    
    prepopulated_fields = {"slug": ('name',) }
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Категории"   
        verbose_name = "Категория"
    
    def get_absolute_url(self):
        return reverse('show_cat', kwargs={'slug_cat': self.slug}) 
        
        
class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # is_publish = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category.name + " " + self.name
    
    class Meta:
        verbose_name_plural = "Продукты"   
        verbose_name = "Продукт"
        ordering = ["name"]
        
        
    def get_absolute_url(self):        
        return reverse('show_products', kwargs={'slug_product': self.slug, 
                                                'slug_cat': self.category.slug
                                                }) 
        