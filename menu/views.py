from django.shortcuts import render,get_object_or_404
from .models import MenuItem,Category

# Create your views here.

def home(request):
    menuitems = MenuItem.objects.all()
    context = {
        'menuitems':menuitems
    }
    return render(request,'home.html',context=context)

def menuitem_detail(request,id):
    menuitem = get_object_or_404(MenuItem,id=id)
    context = {
        'menuitem':menuitem
    }
    return render(request,'menuitem_detail.html',context)




