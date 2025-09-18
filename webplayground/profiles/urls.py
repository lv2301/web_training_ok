from django.urls import path
from .views import ProfileListView, ProfileDetailView, rutina, cuaderno, cuota_view, editar_nota, eliminar_nota


profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('rutina/', rutina, name='rutina'),
    path('cuaderno/', cuaderno, name='cuaderno'),
    path('cuaderno/editar/<int:pk>/', editar_nota, name='editar_nota'),
    path('cuaderno/eliminar/<int:pk>/', eliminar_nota, name='eliminar_nota'),
    path('cuota/', cuota_view, name='cuota'),  # ✅ ahora sí antes del detail
    path('<username>/', ProfileDetailView.as_view(), name='detail'),  # ⬅️ SIEMPRE al final
], "profiles")

