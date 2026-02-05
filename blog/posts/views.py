from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def add_blog(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_home')
    else:
        form=PostForm()
    return render(request,'add.html',{'form':form})

def view_posts(request):
    posts=Post.objects.filter(is_published=True).order_by('-created_date')
    query=request.GET.get('q')
    if query:
        posts=posts.filter(title__icontains=query)
    return render(request,'view_posts.html',{'posts':posts})

def single_post(request,slug):
    post=get_object_or_404(Post,slug=slug,is_published=True)
    return render(request,'post.html',{'post':post})

