from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title': 'first post title',
        'author': 'jenral',
        'date': 'may 2, 2020',
        'content': 'first post content'
    },

    {
        'title': 'second post title',
        'author': 'kweku',
        'date': 'may 4, 2020',
        'content': 'second post content'
    }
]

def home(request):
    context = {
        'posts': posts,
        'pageTitle': 'Home Page'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'pageTitle': 'About Page'})
