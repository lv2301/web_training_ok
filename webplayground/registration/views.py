from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance  # Usuario recién creado

    # Obtener el perfil del usuario (ya creado por la señal post_save) y actualizarlo
        profile, created = Profile.objects.get_or_create(user=user)
        profile.full_name = form.cleaned_data['full_name']
        profile.birth_date = form.cleaned_data['birth_date']
        profile.age = form.cleaned_data['age']
        profile.phone = form.cleaned_data['phone']
        profile.save()

        return response
        

    def get_success_url(self):
        return reverse_lazy('profile')  # ⬅️ Asegura que la redirección sea al dashboard  

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real los widgets de los campos
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})

        form.fields['full_name'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Nombre completo'})
        form.fields['birth_date'].widget = forms.DateInput(
            attrs={'class':'form-control mb-2', 'type': 'date'})
        form.fields['age'].widget = forms.NumberInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Edad'})
        form.fields['phone'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Teléfono'})

        return form


# Vista para Editar el Perfil
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        profile = form.save(commit=False)
        if 'avatar' in self.request.FILES:
            profile.avatar = self.request.FILES['avatar']
        profile.save()
        return super().form_valid(form)



@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form
    

# Vista del Dashboard (Perfil)
@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(user=self.request.user)