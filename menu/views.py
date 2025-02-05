from django.shortcuts import render,get_object_or_404,redirect
from .models import MenuItem,Category,Comment
from .forms import CommentForm
# Create your views here.

def home(request):
    categories = Category.objects.all()
    items = MenuItem.objects.all()
    context = {
        'items':items,
        'categories':categories,
        'selected_category':None
    }
    return render(request,'home.html',context=context)

def item_detail(request, id):
    item = get_object_or_404(MenuItem, id=id)  
    comments = Comment.objects.filter(item=item)  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item  
            comment.author = request.user  #
            comment.save()
            return redirect('item_detail', id=item.id) 
    else:
        form = CommentForm()

    context = {
        'item': item,
        'comments': comments,
        'form': form
    }
    return render(request, 'item_detail.html', context)

def category_filter(request,category_name):
    categories = Category.objects.all()
    category = get_object_or_404(Category,name=category_name)
    items = MenuItem.objects.filter(category=category)
    context = {
        'categories':categories,
        'items':items,
        'selected_category':category.name
    }
    return render(request,'home.html',context=context)



