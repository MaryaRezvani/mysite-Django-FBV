from django import template 
from blog.models import Post
register = template.Library()

@register.simple_tag(name="totalpost")
def function():
    posts = Post.objects.filter(status=1).count()
    return posts
    
@register.simple_tag(name="posts")
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg]