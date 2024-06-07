from django.shortcuts import render



def property_grid(request):
    return render(request,'property/property-grid.html')


def property_single(request):
    return render(request,'property/property-single.html')
