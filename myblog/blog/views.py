from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

class About(ListView):
    template_name = 'blog/about.html'
    queryset = Post.objects.all()