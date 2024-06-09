from django.urls import path
from .views import *
from property.views import property_grid,property_single


app_name = 'agent'



urlpatterns = [
    path('',agents_grid,name='agents-grid'),
    path('agent-singl/<int:id>',agent_single,name='agent-singl'),
    path('agent-single/<int:id>',agent_single,name='agent-single'),
    path('prop/<str:category>',property_grid,name="list_by_category"),
    path('more/<int:id>',property_single,name="list_by_id")
]
