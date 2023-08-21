from django.shortcuts import render,get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post,pk = pid,status=1)
    context = {'post':post}
    #context ={'title':'bitcoin crashed again!','content':'bitcoin was flying but now grounded as always ','author':'Maryam Rezvani'}
    return render(request,'blog/blog-single.html',context)

def test(request):
    # posts = Post.objects.filter(status=1)
    # context = {'posts':posts}
    # post = Post.objects.get(id = pid)
    return render(request,'test.html')


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)








