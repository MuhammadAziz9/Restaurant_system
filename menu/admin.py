from django.contrib import admin
from .models import Category,MenuItem,Comment

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','category']
    list_filter = ['name','price','description','category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Comment)
