from django.contrib import admin
from .models import TrainingRoutine, TrainingDay, TrainingExercise

class TrainingExerciseInline(admin.TabularInline):  # Permite agregar ejercicios dentro de un día
    model = TrainingExercise
    extra = 1

class TrainingDayInline(admin.TabularInline):  # Permite agregar días dentro de una rutina
    model = TrainingDay
    extra = 1

@admin.register(TrainingRoutine)
class TrainingRoutineAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    inlines = [TrainingDayInline]  # Muestra los días dentro de la rutina

@admin.register(TrainingDay)
class TrainingDayAdmin(admin.ModelAdmin):
    list_display = ('routine', 'day_name')
    inlines = [TrainingExerciseInline]  # Muestra los ejercicios dentro del día

@admin.register(TrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    list_display = ('day', 'name', 'sets', 'reps', 'rest_time', 'video_link')
