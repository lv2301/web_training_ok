from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 caracteres como máximo y debe ser válido.")
    full_name = forms.CharField(max_length=255, required=True, help_text="Requerido. Introduce tu nombre completo.")
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), help_text="Requerido. Selecciona tu fecha de nacimiento.")
    age = forms.IntegerField(required=True, help_text="Requerido. Introduce tu edad.")
    phone = forms.CharField(max_length=20, required=True, help_text="Requerido. Introduce tu número de teléfono.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "full_name", "birth_date", "age", "phone")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'full_name', 'birth_date', 'age', 'phone']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nombre completo'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control mt-3', 'type': 'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Edad'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Teléfono'}),
        }





class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email