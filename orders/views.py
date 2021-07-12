from orders.forms import OrderForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from carts.models import CartItem

# Create your views here.


def place_order(request):
    current_user = request.user

    # If cart count is less than or equal to 0,then redirec back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    if request.method == 'POST':
        form = OrderForm(request.POST)
