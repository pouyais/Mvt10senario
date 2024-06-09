from django.urls import path
from .views import *

app_name = 'property'


urlpatterns = [
    path('',property_grid,name='property-grid'),
    path('category/<str:category>',property_grid,name='list_by_category'),
    path('property-single/',property_single,name='property-single'),
]
