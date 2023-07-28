
import scrapy
# from urllib.parse import urlencode
# API_KEY = '630cc9f6-ab1e-40f2-9555-04082a682282'


# def get_scrapeops_url(url):
#     payload = {'api_key': API_KEY, 'url': url}
#     proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
#     return proxy_url


class ScrapySpider(scrapy.Spider):
    name = 'firstCrawl'
    start_urls = [
        "https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656022011&dc&qid=1690447626&rnid=618072011&ref=lp_1000_nr_p_n_feature_browse-bin_0"
    ]

    def parse(self, response):

        # for url in start_urls:
        #     yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)
        title = response.css('.a-color-base.a-text-normal::text').extract()
        yield {'titletext': title}
