from django.urls import path
from .views import mi_rutina

app_name = 'workouts'

urlpatterns = [
    path('mi_rutina/', mi_rutina, name='mi_rutina'),
]
