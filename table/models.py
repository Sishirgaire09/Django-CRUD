from django.db import models



class Category (models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self) -> str:
    return self.name
  
  # Create your models here.
class Product(models.Model):
  product_name = models.CharField(max_length=100)
  category = models.ForeignKey(Category , on_delete=models.CASCADE, null=True, blank=True)    #when deleting product from category it on delete the Product class of its data.
  
