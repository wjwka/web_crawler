import scrapy

class ThreeDSpider(scrapy.Spider):
    name = '3dspider'
    start_urls = ['']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
EOF