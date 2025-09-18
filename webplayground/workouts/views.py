from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TrainingRoutine

@login_required
def mi_rutina(request):
    rutina = TrainingRoutine.objects.filter(user=request.user).first()
    
    # Obtener el número de semana actual desde la URL (por defecto, mostrar la semana 1)
    week_number = int(request.GET.get('week', 1))

    # Filtrar los días de entrenamiento según la semana seleccionada
    days = rutina.days.filter(week_number=week_number) if rutina else None

    # Verificar si existe una semana siguiente
    has_next_week = rutina.days.filter(week_number=week_number + 1).exists() if rutina else False

    return render(request, 'workouts/rutina.html', {
        'rutina': rutina,
        'days': days,
        'current_week': week_number,
        'has_next_week': has_next_week,  # ⬅️ Pasamos esta variable al template
    })
