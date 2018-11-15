from django.shortcuts import render
from django.views import generic
from django.http import *
from .models import *
from django.urls import reverse
# Create your views here.
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

@login_required
def create_post(request):
    query = Post.objects.all()

    if request.POST:
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.POST.get('user')
        real = User.objects.get(id=user)
        obj = Post(post_title=title, post_content=content, writer=real)
        obj.save()
        return HttpResponseRedirect('/blog')
    else:
        return render(request, template_name='blog/create.html', context={'posts':query})

class DeletePost(generic.DeleteView):
    model = Post
    success_url = '/blog'
    template_name = 'blog/confirm_delete.html'
