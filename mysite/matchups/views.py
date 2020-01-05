# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Team, Player
from .forms import TeamForm

# Create your views here.



#TODO use TeamForm object form to get data from user
#TODO create Team objecte team_1 and team_2 from form

def index(request):
    form = TeamForm(request.GET)

    context = {'form': form}

    return render(request, 'matchups/index.html', context = context)

def results(request):

    query_set = []
    query_set.append(request.GET.get('q1'))
    query_set.append(request.GET.get('q2'))

    team_1 = Team(name = query_set[0])
    team_2 = Team(name = query_set[1])

    context = {
        'team_1': team_1,
        'team_2': team_2
    }

    return render(request, 'matchups/results.html', context = context)
