
import scrapy
from scrapy.http import FormRequest
from ..items import ScrapywebsiteItem


class ScrapySpider(scrapy.Spider):
    name = 'firstCrawl'
    start_urls = [
        "https://quotes.toscrape.com/login"
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'nguyengiang20112001@gmail.com',
            'password': '123456'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
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
