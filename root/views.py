from django.shortcuts import render
from .models import Service,Testimonial
from property.models import Propertie
from agent.models import Agent
from blog.models import New





def index(request):

    context = {
        'services' : Service.objects.filter(status=True),
        'properties' : Propertie.objects.filter(status=True),
        'agents' : Agent.objects.filter(status=True),
        'news' : New.objects.filter(status=True),
        'testimonials' : Testimonial.objects.filter(status=True),
    }

    return render(request,'root/index.html',context=context)


def about(request):
    return render(request,'root/about.html')


def contact(request):
    return render(request,'root/contact.html')