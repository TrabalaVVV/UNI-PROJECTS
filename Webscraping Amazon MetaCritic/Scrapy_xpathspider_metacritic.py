import scrapy


class XpathspiderSpider(scrapy.Spider):
    name = "xpathspider"
    allowed_domains = ["metacritic.com"]
    start_urls = ["http://metacritic.com/"]

    def start_requests(self):
        urls = [
            'https://www.metacritic.com/browse/games/score/metascore/all/ps5/filtered',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Loop through each game element on the page
        for game in response.css('.clamp-summary-wrap'):
            # Extract game title, score, and other details
            title = game.xpath('normalize-space(.//div[@class="title"]/h3/text())').get()
            score = game.css('.clamp-metascore .metascore_w::text').get()
            user_score = game.css('.clamp-userscore .metascore_w::text').get()

            # Log extracted data
            self.log(f'Title: {title}, Score: {score}, User Score: {user_score}')

            # Yield the extracted data as a dictionary
            yield {
                'title': title,
                'score': score,
                'user_score': user_score,
            }
