from django.urls import path
from .views import *


app_name = 'agent'



urlpatterns = [
    path('',agent,name='agent'),
    path('single/',agent_single,name='agent-single'),
]
