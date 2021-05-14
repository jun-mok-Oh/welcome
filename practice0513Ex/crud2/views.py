from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html', {'blog' : blog})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.writer = request.POST['writer']
    blog.body = request.POST['body']
    blog.pub_date = timezone.now()
    blog.save()
    return redirect('detail', blog.id)

def edit(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':blog})

def update(request,id):
    blog = Blog.objects.get(id=id)
    blog.title = request.POST['title']
    blog.writer = request.POST['writer']
    blog.body = request.POST['body']
    blog.pub_date = timezone.now
    blog.save()
    return redirect('detail', blog.id)
