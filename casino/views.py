from django.views.generic import ListView
from .models import Post
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(ListView):
    context_object_name = 'home_list'    
    template_name = 'free.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        
        # And so on for more models
        return context

class AboutPageView(TemplateView):
    template_name = 'about-us.html'

class ContactView(TemplateView):
    template_name = 'contact-us.html'