import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=books&i=stripbooks-intl-ship&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&crid=3LQM7CAG6LH20&qid=1690970163&rnid=13054642011&sprefix=books%2Cstripbooks-intl-ship%2C292&ref=sr_nr_p_n_feature_twenty_browse-bin_1&ds=v1%3AfBLgKeBNsK84BUddaR1bF4l74ZK6Pflj70NR8PWId24"]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css(
            ".a-color-base.a-text-normal::text").extract()
        product_author = response.css(
            ".a-color-secondary .a-size-base.s-link-style").css("::text").extract()
        product_price = response.css(
            "#search .a-price span span").css("::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
