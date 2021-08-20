#TODO eliminate unneeded imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date
from urllib.request import urlopen

import certifi
import time
import sys
import json
import re

from .models import Team, Player

#TODO change this to use Scrapy implementation
class Scraper():

    def __init__(self, team):
        self.team = team

    # get basketball reference html page and return array of html tables containing player stats
    def get_stats_tables(self, team):

        # open basketball reference site and store its html in soup
        browser = webdriver.Safari()
        page = urlopen("https://www.basketball-reference.com/", cafile=certifi.where())
        soup = BeautifulSoup(page, 'html.parser')

        #go thru soup and extract json object containing list of players
        script_tags = soup.findAll("script", class_= "allowed")

        #format json
        formatted_json = "/n".join((script_tags[1])).split("\n",2)[2];
        formatted_json = "{" + formatted_json[formatted_json.find('\n')+1:formatted_json.rfind('\n')]
        formatted_json = formatted_json[:-1]

        json_obj = json.loads(formatted_json)

        players_json = json_obj[team.get_city()]

        # go thru players_json and scrape url addresses
        # add to list(player_urls) holding url addresses of each player
        length = len(players_json)
        player_urls = []
        for i in range(length):
            for key, value in players_json[i].items():
                player_urls.append(key)

        # go thru player_urls and scrape table containing player stats
        # add to player_tables
        player_tables = []
        length = len(player_urls)
        for i in range(length):
            print(player_urls[i])

            # query the website and store the html in page
            url = "https://www.basketball-reference.com" + player_urls[i]
            page = urlopen(url, cafile=certifi.where())
            browser.get(url)
            soup = BeautifulSoup(page, 'html.parser')

            # get html table containing current years stats
            curr_year = date.today().year
            stats_table = soup.find("tr", attrs={"id":"per_game." + str(curr_year)})
            if stats_table is not None:
                stats_table = stats_table.find_all("td", attrs={"class":"right"})

            player_tables.append(stats_table)
        browser.close()

        return player_tables

    # populate stats fields in a Player model based on table
    def populate_player_stats(self, table, player):

        for cell in table:
            print(cell)
            for field in player._meta.get_fields():
                if str(field.name) in str(cell):
                    stat = re.findall("\d+\.\d+", str(cell))
                    setattr(player, str(field.name), float(stat[0]))
                    player.save()
        return player

    # populate fields(game_score) in Team model
    def populate_team(self):

        player_tables = self.get_stats_tables(self.team)

        length = len(player_tables)
        tot_game_score = 0

        for i in range(length):
            if(player_tables[i] is not None):
                player = Player.objects.create_player()
                player = self.populate_player_stats(player_tables[i], player)
                tot_game_score += player.game_score()
                print(player.game_score())

        setattr(self.team, 'game_score', tot_game_score)
        self.team.save()
