import scrapy
from scraper.items import TeamItem
from scraper.items import PlayerItem

#TODO
class StatsSpider(scrapy.Spider):
    name = "stats"

    def start_requests(self):
        #TODO add individual player addresses
        ursl = ["https://www.basketball-reference.com/"]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page = response.url.split("/")
        filename = f'stats-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
