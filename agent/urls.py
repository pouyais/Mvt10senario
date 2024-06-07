from django.urls import path
from .views import *


app_name = 'agent'



urlpatterns = [
    path('',agents_grid,name='agents-grid'),
    path('agent-single/',agent_single,name='agent-single'),
]
