from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название продукта')
    price = models.IntegerField(verbose_name='цена продукта')
    description = models.CharField(max_length=250, verbose_name='описание продукта')
    image = models.ImageField(blank=True, upload_to='my_images')
    
    def __str__(self):
        return f"{self.name} по цене {self.price} "
