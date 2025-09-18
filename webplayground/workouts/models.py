from django.db import models
from django.contrib.auth.models import User

class TrainingRoutine(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Cada usuario tiene su rutina
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Última actualización

    def __str__(self):
        return f"Rutina de {self.user.username}"

class TrainingDay(models.Model):
    routine = models.ForeignKey(TrainingRoutine, on_delete=models.CASCADE, related_name="days")  # Relación con la rutina
    week_number = models.PositiveIntegerField(default=1)  # ⬅️ Indica la semana
    day_name = models.CharField(max_length=20)  # Nombre del día (Día 1, Lunes, etc.)


    class Meta:
        ordering = ['week_number', 'day_name']  # Ordenar primero por semana y luego por día

    def __str__(self):
        return f"Semana {self.week_number} - {self.day_name} ({self.routine.user.username})"
    
    

class TrainingExercise(models.Model):
    day = models.ForeignKey(TrainingDay, on_delete=models.CASCADE, related_name="exercises")  # Relación con el día
    name = models.CharField(max_length=100)  # Nombre del ejercicio
    sets = models.PositiveIntegerField()  # Número de series
    reps = models.CharField(max_length=50)  # Repeticiones (puede ser "10-12", "hasta el fallo", etc.)
    rest_time = models.CharField(max_length=50)  # Tiempo de descanso entre series
    video_link = models.URLField(blank=True, null=True)  # Enlace a video de YouTube (opcional)

    def __str__(self):
        return f"{self.day.day_name} - {self.name}"
