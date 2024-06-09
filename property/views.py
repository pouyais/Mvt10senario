from django.shortcuts import render
from .models import Propertie,Category_property



def property_grid(request,**kwargs):

    if kwargs.get('category'):
        prop = Category_property.objects.filter(title=kwargs.get('category'))
    else:
        prop = Category_property.objects.all()

    context = {
        'category' : prop,
        # 'category' : Category_property.objects.filter(status=True),
    }

    return render(request,'property/property-grid.html',context=context)


def property_single(request):
    return render(request,'property/property-single.html')
