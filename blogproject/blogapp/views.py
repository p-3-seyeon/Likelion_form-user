from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})
    
def detail(request, id):
    details = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'details':details})

# new.html을 띄워주는 함수
def new(request): 
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

 # 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, id):
    edit_blog = get_object_or_404(Blog, id=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = get_object_or_404(Blog, id=id)
    update_blog.title = request.POST['title']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', str(update_blog.id))

def delete(request, id):
    delete_blog = get_object_or_404(Blog, id=id)
    delete_blog.delete()
    return redirect('home')

