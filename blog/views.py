from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
         'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
     return render(request, 'about/home.html', {'title': 'About'})

