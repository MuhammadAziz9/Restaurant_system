from django.db import models
from django.contrib.auth import get_user_model
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
    
class Comment(models.Model):
    item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __srt__(self):
        return self.comment
