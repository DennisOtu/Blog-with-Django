from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    context = {
        'posts': Post.objects.all(),
        'pageTitle': 'Home Page'
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html', {'pageTitle': 'About Page'})
