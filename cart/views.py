from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from product.models import Products
from .cart import Cart
from .models import OrderProduct


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

 # TODO переделать cart_detail в класс
# class ProdCart(ListView):
#     model = Cart
#     context_object_name = 'cart'
#     template_name = 'cart/cart.html'
#     raise_exception = True
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Корзина товаров'
#         return context


def add_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    Cart(request).add(product=product)
    return redirect(request.META['HTTP_REFERER'])  # возвращаем на текущую страницу


def decrement_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    Cart(request).decrement(product=product)
    return redirect(request.META['HTTP_REFERER'])


def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect(request.META['HTTP_REFERER'])


def order_create(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        for item in cart:
            OrderProduct.objects.create(user=request.user,
                                        product=item['product'],
                                        quantity=item['quantity'])
        cart.clear()
        return render(request, '')
    else:
        return redirect('user_data:login')
