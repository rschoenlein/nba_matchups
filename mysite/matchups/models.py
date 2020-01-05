# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# models representing players, and teams with associated stats
# essentially our database layout
# each field is stored in SQL database as a column name


class Team(models.Model):

    NAME_CHOICES = (
        ('Celtics', 'Celtics'),
        ('Hawks', 'Hawks'),
        ('Warriors', 'Warriors'),
        ('Hornets', 'Hornets'),
        ('Bulls', 'Bulls'),
        ('Cavaliers', 'Cavaliers'),
        ('Mavericks', 'Mavericks'),
        ('Nuggets', 'Nuggets'),
        ('Pistons', 'Pistons'),
        ('Rockets', 'Rockets'),
        ('Pacers', 'Pacers'),
        ('Clippers', 'Clippers'),
        ('Lakers', 'Lakers'),
        ('Grizzlies', 'Grizzlies'),
        ('Heat', 'Heat'),
        ('Bucks', 'Bucks'),
        ('Timberwolves', 'Timberwolves'),
        ('Pelicans', 'Pelicans'),
        ('Knicks', 'Knicks'),
        ('Thunder', 'Thunder'),
        ('Magic', 'Magic'),
        ('Sixers', 'Sixers'),
        ('Suns', 'Suns'),
        ('Kings', 'Kings'),
        ('Spurs', 'Spurs'),
        ('Raptors', 'Raptors'),
        ('Jazz', 'Jazz'),
        ('Wizards', 'Wizards')
    )

    name = models.CharField(max_length = 200, choices = NAME_CHOICES)

    #team name to city dictionary
    team_cities = {
        "Celtics": "BOS",
        "Hawks": "ATL",
        "Warriors": "GSW",
        "Nets": "BKN",
        "Hornets": "CHA",
        "Bulls": "CHI",
        "Cavaliers": "CLE",
        "Mavericks": "DAL",
        "Nuggets": "DEN",
        "Pistons": "DET",
        "Rockets": "HOU",
        "Pacers": "IND",
        "Clippers": "LAC",
        "Lakers": "LAL",
        "Grizzlies": "MEM",
        "Heat": "MIA",
        "Bucks": "MIL",
        "Timberwolves": "MIN",
        "Pelicans": "NOP",
        "Knicks": "NYK",
        "Thunder": "OKC",
        "Magic": "ORL",
        "Sixers": "PHI",
        "Suns": "PHX",
        "Blazers": "POR",
        "Kings": "SAC",
        "Spurs": "SAS",
        "Raptors": "TOR",
        "Jazz": "UTA",
        "Wizards": "WAS"
    }

    def get_city(self):
        return team_cities[self.name]

    def __str__(self):
        return self.name

class Player(models.Model):

    name = models.CharField(max_length = 200)

    #stats
    pts_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    fg_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    fga_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    ft_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    fta_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    drb_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    orb_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    stl_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    ast_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    blk_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    pf_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)
    tov_per_g = models.DecimalField(decimal_places = 3, max_digits = 6, default = 1.0)

    current_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def game_score(self):
        return self.pts_per_g + 0.4*self.fg_per_g - 0.7*self.fga_per_g- 0.4*(self.fga_per_g - self.ft_per_g)  + 0.7*self.orb_per_g + 0.3*self.drb_per_g + self.stl_per_g + 0.7*self.ast_per_g + 0.7*self.blk_per_g - 0.4*self.pf_per_g - self.tov_per_g;

    def __str__(self):
        return self.name


class Matchup(models.Model):
    result = models.CharField(max_length = 200)

    def __str__(self):
        return self.result
