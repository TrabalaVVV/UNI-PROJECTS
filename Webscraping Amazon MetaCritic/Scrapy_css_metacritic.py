import scrapy
from scrapy.item import Item, Field

class Game(Item):
    title = Field()
    platform = Field()

class MetacriticSpider(scrapy.Spider):
    name = "css_listing"
    start_urls = [
        "https://www.metacritic.com/browse/games/genre/date/action/all"
    ]

    def parse(self, response):
        for game in response.css(".clamp-summary-wrap"):
            item = Game()
            item["title"] = game.css(".title h3::text").get()
            item["platform"] = game.css(".clamp-details .platform .data::text").get()

            yield item
