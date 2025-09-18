from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'is_client')  # ⬅️ Mostrar en la lista
    list_filter = ('is_client',)  # ⬅️ Filtro por clientes
    search_fields = ('user__username', 'full_name')

admin.site.register(Profile, ProfileAdmin)
