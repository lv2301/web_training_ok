from django.contrib import admin
from .models import Product,Category, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'featured', 'created_at')
    list_filter = ('available', 'featured')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'get_total_price')

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = "Total por ítem"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'paid', 'get_total')
    list_filter = ('paid', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]
    readonly_fields = ('user', 'created_at', 'get_total')

    def get_total(self, obj):
        return f"${obj.get_total():.2f}"
    get_total.short_description = "Total"