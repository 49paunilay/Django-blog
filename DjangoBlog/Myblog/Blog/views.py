from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()[::-1]
   # print(allpost)
    context={
        'allpost':allpost,
    }
    return render(request,'blog/blog.html',context)

def blogPost(request,slug):
    thepost = Post.objects.filter(addressdlug=slug).first()

    context={
        'thepost':thepost,

    }
    return render(request,'blog/blogPost.html',context)
