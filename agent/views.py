from django.shortcuts import render
from .models import Agent



def agents_grid(request):


    context = {
        'agents' : Agent.objects.filter(status=True)
    }

    return render(request,'agent/agents-grid.html',context=context)


def agent_single(request):
    return render(request,'agent/agent-single.html')