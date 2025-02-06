# views.py
# from django.shortcuts import render, redirect
# from .models import Order, OrderItem
# from .forms import OrderForm
# from menu.models import MenuItem

# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.customer = request.user  # Foydalanuvchi kimligini olish
#             order.save()
            
#             # Buyurtma elementlarini qo'shish (order_item larni yaratish)
#             order_items = request.POST.getlist('items')  # misol uchun, buyurtmalarni olish
#             total_price = 0
#             for item_id in order_items:
#                 item = MenuItem.objects.get(id=item_id)
#                 order_item = OrderItem(order=order, menu_item=item, quantity=1, price=item.price)
#                 order_item.save()
#                 total_price += item.price  # Totalni hisoblash
            
#             order.total_price = total_price
#             order.save()
            
#             return redirect('order_success')  # muvaffaqiyatli buyurtma sahifasiga yo'naltirish
#     else:
#         form = OrderForm()
#     return render(request, 'order/create_order.html', {'form': form})

