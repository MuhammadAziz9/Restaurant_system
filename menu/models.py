from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu_images')

    def __str__(self):
        return self.name
