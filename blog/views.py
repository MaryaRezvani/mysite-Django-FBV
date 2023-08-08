from django.shortcuts import render,get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    context ={'title':'bitcoin crashed again!','content':'bitcoin was flying but now grounded as always ','author':'Maryam Rezvani'}
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    #post = Post.objects.get(id = pid)
    post = get_object_or_404(Post,pk = pid)
    context = {'post':post}
    return render(request,'test.html',context)





