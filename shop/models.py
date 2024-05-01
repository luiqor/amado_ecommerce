from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category (models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)   
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Brand (models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'brands' 

    def __str__(self):
        return self.name


class Item (models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    stars = models.IntegerField(default=0,
        validators=[MaxValueValidator(5), 
                    MinValueValidator(0)]
        )
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='item', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'items'
        ordering = ('price','-price', 'created', '-created', 'stars', '-stars')

    def __str__(self):
        return self.name
