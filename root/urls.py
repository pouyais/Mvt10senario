from django.urls import path
from .views import *
from property.views import property_single
from agent.views import agent_single
from blog.views import blog_single

app_name = 'root'


urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('proper/<int:id>',property_single,name="list_by_id"),
    path('person/<int:id>',agent_single,name='list_by_person'),
    path('news/<int:id>',blog_single,name='list_by_blog')
]
