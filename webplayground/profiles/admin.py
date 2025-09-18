from django.contrib import admin
from .models import CuotaMensual

@admin.register(CuotaMensual)
class CuotaMensualAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_inicio', 'fecha_vencimiento', 'monto', 'pagado')
    list_filter = ('pagado', 'fecha_inicio', 'fecha_vencimiento')
    search_fields = ('user__username',)
    ordering = ('-fecha_inicio',)
