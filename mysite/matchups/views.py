# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Team, Player, Matchup
from .forms import TeamForm
from .scraper import Scraper


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


        predicted_score = []
        team_1 = Team.objects.create_team(query_set[0])
        team_2 = Team.objects.create_team(query_set[1])

        scraper = Scraper(team_1)
        scraper.populate_team()
        predicted_score.append(1.4 * team_1.game_score)

        scraper = Scraper(team_2)
        scraper.populate_team()
        predicted_score.append(1.4 * team_2.game_score)

        matchup = Matchup.objects.create_matchup(team_1, team_2)
        winner = matchup.get_winner()

        #pass teams, winner and scores to results.html
        context = {
            'team_1': team_1,
            'team_2': team_2,
            'winner': winner,
            'score_1': predicted_score[0],
            'score_2': predicted_score[1]
        }

        return render(request, self.template_name, context = context)
