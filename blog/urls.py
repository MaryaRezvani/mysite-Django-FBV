from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    #path('url address', 'view', 'name' )
    path('', blog_view,name='index'),
    path('<int:pid>', blog_single,name='single'),
    path('category/<str:cat_name>', blog_category,name='category'),
    #path('post-<int:pid>', test,name='test'),
    path('test', test,name='test'),

]