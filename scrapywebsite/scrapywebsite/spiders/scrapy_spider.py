
import scrapy
from ..items import ScrapywebsiteItem


class ScrapySpider(scrapy.Spider):
    name = 'firstCrawl'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):

        items = ScrapywebsiteItem()

        all_div_quotes = response.css('div.quote')

        for item in all_div_quotes:

            title = item.css('span.text::text').extract()
            author = item.css('.author::text').extract()
            tag = item.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
