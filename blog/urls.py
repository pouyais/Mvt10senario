from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    path('',blog_grid,name='blog-grid'),
    path('blog-single/',blog_single,name='blog-single')
]
