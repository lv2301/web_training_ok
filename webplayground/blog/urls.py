from django.urls import path
from .views import PostListView, PostDetailView, AddCommentView

urlpatterns = [
    path('', PostListView.as_view(), name='blog_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='blog_detail'),
    path('<slug:slug>/comment/', AddCommentView.as_view(), name='add_comment'),  # Nueva ruta para comentarios
]
