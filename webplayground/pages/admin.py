from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'image_preview','price', 'mostrar_precio')  # Agregamos un campo para previsualizar la imagen

    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" width="100" />'.format(obj.image.url)  # Muestra una miniatura de la imagen
        return "No image"
    image_preview.allow_tags = True  # Permite renderizar el HTML (la miniatura de la imagen)

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
