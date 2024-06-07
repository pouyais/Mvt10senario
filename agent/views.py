from django.shortcuts import render



def agent(request):
    return render(request,'agent/agents-grid.html')


def agent_single(request):
    return render(request,'agent/agent-single.html')