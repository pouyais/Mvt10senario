from django.urls import path
from .views import *

app_name = 'property'


urlpatterns = [
    path('',property_grid,name='property-grid'),
    path('category/<str:category>',property_grid,name='list_by_category'),
    path('rent/<int:rent>',property_grid,name='list_by_rent'),
    path('property-singl/',property_singl,name='property-singl'),
    path('property-single/<int:id>',property_single,name="list_by_property_id"),
]
