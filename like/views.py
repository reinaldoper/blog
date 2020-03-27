from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BlogForm
from .models import Blog


def index(request):
    list = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(list, 3)
    page = request.GET.get('page')
    list = paginator.get_page(page)
    return render(request, 'index.html',{'list':list})


def add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = BlogForm()
        return render(request,'list.html',{'form':form})
# Create your views here.
