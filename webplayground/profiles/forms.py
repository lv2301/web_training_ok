from django import forms
from registration.models import TrainingNote

class TrainingNoteForm(forms.ModelForm):
    class Meta:
        model = TrainingNote
        fields = ['content']
        labels = {
            'content': '',  # oculta el label visual
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escribí tu avance, comentario o recordatorio...',
                'style': 'resize:none;'
            }),
        }
