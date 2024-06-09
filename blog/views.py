from django.shortcuts import render
from .models import New
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def blog_grid(request,**kwargs):

    if kwargs.get('blog'):
        new = New.objects.filter(title=kwargs.get('blog'))
    else:
        new = New.objects.filter(status=True)

    all = Paginator(new,3)
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
        'news' : all,
        'last_page' : last_page
    }


    return render(request,'blog/blog-grid.html',context=context)


def blog_single(request,id):

    blogs = New.objects.get(id=id)

    context = {
        'blog' : blogs
    }

    return render(request,'blog/blog-single.html',context=context)





def blog_singl(request):


    return render(request,'blog/blog-single.html')