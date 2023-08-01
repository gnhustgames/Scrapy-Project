
import scrapy
from ..items import ScrapywebsiteItem


class ScrapySpider(scrapy.Spider):
    name = 'firstCrawl'
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
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
        # next_page = response.css('li.next a::attr(href)').get()
        next_page = 'https://quotes.toscrape.com/page/' + \
            str(ScrapySpider.page_number)+'/'
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        if ScrapySpider.page_number < 11:
            ScrapySpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
