from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import TrainingNoteForm
from registration.models import TrainingNote
from .models import CuotaMensual
from urllib.parse import quote
from django.contrib import messages



# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 6



class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
    


@login_required
def rutina(request):
    if not request.user.profile.is_client:
        return render(request, 'profiles/acceso_restringido.html')

    # Procesar el formulario si se envía
    if request.method == "POST":
        form = TrainingNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Asociar la nota con el usuario logueado
            note.save()
            return redirect('profiles:rutina')  # Recargar la página

    else:
        form = TrainingNoteForm()

    # Obtener las notas del usuario
    rutina = TrainingNote.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'profiles/rutina.html', {'form': form, 'rutina': rutina})



@login_required
def cuaderno(request):
    if not request.user.profile.is_client:
        return render(request, 'profiles/acceso_restringido.html')

    if request.method == "POST":
        form = TrainingNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('profiles:cuaderno')

    else:
        form = TrainingNoteForm()

    notes = TrainingNote.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'profiles/cuaderno.html', {'form': form, 'notes': notes})



@login_required
def editar_nota(request, pk):
    note = get_object_or_404(TrainingNote, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TrainingNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Nota actualizada correctamente.")
            return redirect('profiles:cuaderno')
    else:
        form = TrainingNoteForm(instance=note)

    return render(request, 'profiles/editar_nota.html', {'form': form})



@login_required
def eliminar_nota(request, pk):
    note = get_object_or_404(TrainingNote, pk=pk, user=request.user)

    if request.method == 'POST':
        note.delete()
        messages.success(request, "Nota eliminada.")
        return redirect('profiles:cuaderno')

    return render(request, 'profiles/eliminar_nota.html', {'note': note})




@login_required
def cuota_view(request):
    # Buscar SOLO las cuotas del usuario logueado
    cuota = CuotaMensual.objects.filter(user=request.user).order_by('-fecha_inicio').first()

    whatsapp_url = None
    if cuota and not cuota.pagado:
        message = (
            f"¡Hola! Soy {request.user.username} y quiero pagar mi cuota mensual:\n\n"
            f"- Monto: ${cuota.monto}\n"
            f"- Desde: {cuota.fecha_inicio.strftime('%d/%m/%Y')}\n"
            f"- Hasta: {cuota.fecha_vencimiento.strftime('%d/%m/%Y')}\n"
        )
        phone = "5493511234567"  # tu número
        whatsapp_url = f"https://wa.me/{phone}?text={quote(message)}"

    return render(request, 'profiles/cuota.html', {
        'cuota': cuota,
        'whatsapp_url': whatsapp_url
    })