from django.db import models
from django.urls import reverse


class Store(models.Model):
    name = models.CharField(max_length=100, unique=True,null=True,blank=True)
    code = models.CharField(max_length=10,null=True,blank=True)
    city_name = models.CharField(max_length=88,null=True,blank=True)
    status = models.BooleanField(default=True,null=True,blank=True)
  
    def __str__(self):
        return self.name
    
    def get_city_products(self):
        pass

    def get_city_cats(self):
        pass

    def get_city_stores(Self):
        pass


class Category(models.Model):
    name=models.CharField(max_length=25)
    slug=models.SlugField(unique=True,max_length=200)

    class Meta:
        ordering=['name']
        indexes=[models.Index(fields=['name']),]
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])


class Product(models.Model):
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name='store_products', null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cat_products',null=True,blank=True)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    # endi ee raydam space leda = + before after 
    class Meta:
        ordering=['name']
        indexes=[models.Index(fields=['id','slug']),models.Index(fields=['name']),models.Index(fields=['-created'])]

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])


