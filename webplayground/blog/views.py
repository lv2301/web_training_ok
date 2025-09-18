from django.contrib.auth.mixins import LoginRequiredMixin  # Para requerir login en CBV
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from blog.models import Post  # Importar Post normal
try:
    from blog.models import Comment  # Intentar importar Comment
except ImportError:
    Comment = None  # Evitar que el editor lo marque como error
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 6  # Paginación: 6 posts por página

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

# Vista para manejar los comentarios
class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('blog_detail', kwargs={'slug': post.slug}) + "#comentarios")

        return HttpResponseRedirect(reverse('blog_detail', kwargs={'slug': post.slug}))
