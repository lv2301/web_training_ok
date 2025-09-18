from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate, ProfileDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileDetailView.as_view(), name="profile"),  # ⬅️ Dashboard único
    path('profile/edit/', ProfileUpdate.as_view(), name="profile_edit"),  # ⬅️ Edición de perfil
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
]
