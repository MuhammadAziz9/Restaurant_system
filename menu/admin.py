from django.contrib import admin
from .models import Category,MenuItem

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','category']
    list_filter = ['name','price','description','category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
