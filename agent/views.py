from django.shortcuts import render



def agents_grid(request):
    return render(request,'agent/agents-grid.html')


def agent_single(request):
    return render(request,'agent/agent-single.html')