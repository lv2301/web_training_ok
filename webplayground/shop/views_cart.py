from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart
from shop.models import Order, OrderItem
from urllib.parse import quote




@login_required
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('shop:cart_detail')


@login_required
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')


@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart_detail.html', {'cart': cart})



@login_required
def checkout(request):
    cart = Cart(request)
    if not cart:
        return redirect('shop:cart_detail')

    order = Order.objects.create(user=request.user)

    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            price=item['product'].price
        )

    cart.clear()
    return render(request, 'shop/checkout_success.html', {'order': order})



@login_required
def checkout_redirect_to_whatsapp(request):
    cart = Cart(request)
    if not cart:
        return redirect('shop:cart_detail')

    # Crear la orden
    order = Order.objects.create(user=request.user)
    message = "¡Hola! Quiero confirmar mi pedido:\n\n"

    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            price=item['product'].price
        )
        message += f"- {item['product'].name} x{item['quantity']} = ${item['total_price']:.2f}\n"

    total = cart.get_total_price()
    message += f"\nTotal: ${total:.2f}\n"
    message += f"Número de pedido: #{order.id}\n\n¿Cómo seguimos con el pago?"

    # Limpiar carrito
    cart.clear()

    # Generar URL de WhatsApp
    phone = "5493511234567"  # ← tu número real
    whatsapp_url = f"https://wa.me/{phone}?text={quote(message)}"

    # Redirigir a página intermedia
    return render(request, 'shop/redirect_to_whatsapp.html', {'whatsapp_url': whatsapp_url})

