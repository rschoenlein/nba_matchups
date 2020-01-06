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

class Scraper():

    #member objects
    player = Player()

    #gets basketball reference html page(soup) and return array of html tables containing player stats
    #TODO replace user_team with team model
    #def get_stats_table(team)
    def get_stats_table(self, user_team):

        #open basketball reference site and store its html in soup
        browser = webdriver.Safari()
        page = urlopen("https://www.basketball-reference.com/", cafile=certifi.where())
        soup = BeautifulSoup(page, 'html.parser')

        #go thru soup and extract json object containing list of players
        script = soup.findAll("script", class_= "allowed")
        raw = "/n".join((script[1])).split("\n",2)[2];
        raw = "{" + raw[raw.find('\n')+1:raw.rfind('\n')]
        raw = raw[:-1]
        json_obj = json.loads(raw)
        players_json = json_obj[Team.team_cities[user_team]]

        #go thru players_json and add to list(player_urls) holding url address of each player
        length = len(players_json)
        player_urls = []
        for i in range(length):
            for key, value in players_json[i].items():
                player_urls.append(key)

        #go thru player_urls and scrape table containing player stats
        #add to player_tables
        player_tables = []
        length = len(player_urls)
        for i in range(length):
            print(player_urls[i])

            #query the website and store the html in page
            url = "https://www.basketball-reference.com" + player_urls[i]
            page = urlopen(url, cafile=certifi.where())
            browser.get(url)
            soup = BeautifulSoup(page, 'html.parser')

            #get html table containing current years stats
            curr_year = date.today().year
            stats_table = soup.find("tr", attrs={"id":"per_game." + str(curr_year)})
            if stats_table is not None:
                stats_table = stats_table.find_all("td", attrs={"class":"right"})


            player_tables.append(stats_table)
        browser.close()

        return player_tables

    #TODO
    #populate stats fields in a Player model based on html table
    # def populate_player(player, table):
    def get_game_score(self, table):

        #dict containg relevent stats
        stats =	{
            "pts_per_g": 0,
            "fg_per_g": 0,
            "fga_per_g": 0,
            "fta_per_g": 0,
            "ft_per_g": 0,
            "orb_per_g": 0,
            "drb_per_g": 0,
            "stl_per_g": 0,
            "orb_per_g": 0,
            "ast_per_g": 0,
            "blk_per_g": 0,
            "pf_per_g": 0,
            "tov_per_g": 0
        }

        #traverse table and scrape stats
        for cell in table:
            for key in stats.keys():
                if key in str(cell):
                        stat = re.findall("\d+\.\d+", str(cell))
                        stats[key] = float(stat[0])

    #TODO
    #populate fields in Team model
    # def populate_team(team):
    def search(self):

        #get total game score for team 1
        player_tables = self.get_stats_table("Lakers")

        length = len(player_tables)
        tot_game_score_1 = 0

        for i in range(length):

            html_table = player_tables[i]
            #parse html_table and calculate game_score
            if(html_table is not None):
                tot_game_score_1 += self.get_game_score(html_table)
