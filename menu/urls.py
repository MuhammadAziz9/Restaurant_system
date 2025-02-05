from django.urls import path
from .views import home,item_detail,category_filter

urlpatterns = [
    path('',home,name='home'),
    path('menuitem/<int:id>/',item_detail,name='item_detail'),
    path('category/<str:category_name>/',category_filter,name='category')
]