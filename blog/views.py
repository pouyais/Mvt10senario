from django.shortcuts import render


def blog_grid(request):
    return render(request,'blog/blog-grid.html')


def blog_single(request):
    return render(request,'blog/blog-single.html')
