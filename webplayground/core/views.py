from django.views.generic.base import TemplateView
from django.shortcuts import render
from blog.models import Post
from pages.models import Page  # Importá tu modelo Page
from shop.models import Product


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.order_by('-created_at')[:2]
        context['servicios'] = Page.objects.order_by('order')[:3]
        context['destacados'] = Product.objects.filter(available=True)[:5]  # 👈 agregamos productos
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = "LV-TRAINER"
        return render(request, self.template_name, context)
    


class ContactPageView(TemplateView):
    template_name = "core/contact.html"
    
