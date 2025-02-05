from django.urls import path
from .views import home,menuitem_detail

urlpatterns = [
    path('',home,name='home'),
    path('menuitem/<int:id>/',menuitem_detail,name='menuitem_detail'),
]