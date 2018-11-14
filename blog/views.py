from django.shortcuts import render
from django.views import generic
from django.http import *
from .models import *
# Create your views here.
def index(request):
    obj = Post.objects.all()
    return render(request, template_name='blog/index.html', context={'obj':obj})

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()