# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Team, Player, Matchup

#TODO customize the display of model objects in admin site
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Matchup)
