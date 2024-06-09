from django.shortcuts import render
from .models import Propertie,Category_property
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def property_grid(request,**kwargs):

    if kwargs.get('category'):
        prop = Propertie.objects.filter(category__title=kwargs.get('category'))
    elif kwargs.get('rent'):
        prop = Propertie.objects.filter(rent__lte=kwargs.get('rent'))
    else:
        prop = Propertie.objects.filter(status=True)

    all = Paginator(prop,3)
    first_page = 1
    last_page = all.num_pages

    try:
        page_number = request.GET.get('page')
        all = all.get_page(page_number)
    except PageNotAnInteger:
        all = all.get_page(1)
    except EmptyPage:
        all = all.get_page(1)


    context = {
        'properties' : all,
        'category' : Category_property.objects.all(),
        'last_page' : last_page,
    }

    return render(request,'property/property-grid.html',context=context)


def property_single(request,id):

    prop = Propertie.objects.get(id=id)

    context = {
        'detail' : prop
    }
    return render(request,'property/property-single.html',context=context)


def property_singl(request):
    return render(request,'property/property-single.html')
