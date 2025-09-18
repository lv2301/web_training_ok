from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'content', 'image', 'order', 'price', 'mostrar_precio']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden  '}),
        }
        labels = {
            'title': '', 'order': '', 'content': '', 'image': 'Imagen'  # Etiqueta para el campo de imagen
        }
