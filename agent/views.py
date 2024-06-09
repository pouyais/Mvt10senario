from django.shortcuts import render
from .models import Agent
from property.models import Propertie,Category_property



def agents_grid(request,):


    agent = Agent.objects.filter(status=True)


    context = {
        'agents' : agent
    }

    return render(request,'agent/agents-grid.html',context=context)


def agent_single(request,id):

    agent = Agent.objects.get(id=id)

    context = {
        'agent' : agent,
        'prop' : Propertie.objects.filter(status=True),
        'category' : Category_property.objects.filter(status=True)
    }

    return render(request,'agent/agent-single.html',context=context)



def agent_singl(request):
    return render(request,'agent/agent-single.html')