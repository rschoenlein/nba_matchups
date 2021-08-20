# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from matchups.models import Team
from matchups.models import Player


class TeamItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Team

class PlayerItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Player
