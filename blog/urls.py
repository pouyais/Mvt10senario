from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    path('',blog_grid,name='blog-grid'),
    path('blog/<str:blog>',blog_grid,name='list_by_blog'),
    path('blog-singl/',blog_singl,name='blog-singl'),
    path('blog-single/<int:id>',blog_single,name='list_by_sblog'),
]
