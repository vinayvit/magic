from django.views.generic import ListView
from .models import Post
from .models import Posttop
from .models import Posttopsecond
from .models import Postlive
from .models import Postslot
from django.shortcuts import render


class IndexView(ListView):
    context_object_name = 'home_list'    
    template_name = 'home.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posttop'] = Posttop.objects.all()
        context['posttopsecond'] = Posttopsecond.objects.all()
        context['postlive'] = Postlive.objects.all()
        context['Postslot'] = Postslot.objects.all()		
        # And so on for more models
        return context


