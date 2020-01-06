# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Team, Player
from .forms import TeamForm
from .scrape import Scraper




class IndexView(generic.ListView):

    template_name = 'matchups/index.html'

    def get(self, request):

        #create form and pass it to index.html
        form = TeamForm(request.GET)

        context = {'form': form}

        return render(request, self.template_name, context = context)


class ResultsView(generic.ListView):

    template_name = 'matchups/results.html'

    def get(self, request):

        #create team objects based on GET query
        query_set = []
        query_set.append(request.GET.get('q1'))
        query_set.append(request.GET.get('q2'))

        team_1 = Team(name = query_set[0])
        team_2 = Team(name = query_set[1])

        #TODO create Scraper object
        #TODO matchup object from Scraper member functions

        scraper = Scraper()
        scraper.search()

        #pass team objects to results.html
        context = {
            'team_1': team_1,
            'team_2': team_2
        }

        return render(request, self.template_name, context = context)
