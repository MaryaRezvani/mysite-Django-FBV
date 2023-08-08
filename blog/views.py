from django.shortcuts import render
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    context ={'title':'bitcoin crashed again!','content':'bitcoin was flying but now grounded as always ','author':'Maryam Rezvani'}
    return render(request,'blog/blog-single.html',context)

def test(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'test.html',context)





