from django.urls import path
from . import views
from . import views_cart

app_name = 'shop'

urlpatterns = [
    path('product_list', views.ProductListView.as_view(), name='product_list'),
    path('cart/', views_cart.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views_cart.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views_cart.cart_remove, name='cart_remove'),
    path('cart/checkout/', views_cart.checkout, name='checkout'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),  # <-- Dejá esta al final
    path('checkout/whatsapp/', views_cart.checkout_redirect_to_whatsapp, name='checkout_whatsapp'),
]

