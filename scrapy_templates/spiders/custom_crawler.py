from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import datetime as dt
import logging
from ..items import ProductItem
from ..config import iamge_path


class ProductCrawler(CrawlSpider):
    name = "custom_crawler1"
    allowed_domains = ["test.com"]
    start_urls = ["test.com/page1"]

    custom_settings = {
        'ITEM_PIPELINES': {
            'product_scraper.pipelines.CustomImageNamePipeline': 1,
            'product_scraper.pipelines.CleaningPipeline': 2,
            'product_scraper.pipelines.SaveProductPipeline': 3
        },
        'IMAGES_STORE': iamge_path
    }

    rules = (
        # go to different categories
        Rule(LinkExtractor(
            allow=('/products/',),
            deny=('/products/secret',),
        ),
            follow=True),
        # step into individual pages
        Rule(LinkExtractor(allow=('/products/specific_products/',)),
             callback='parse_item',),
    )

    def parse_item(self, response):
        """ Scraping items and passing them through the pipeline.

        Args:
            response: response from the server

        Returns:
            Yielding the scrapy item class called ProductScraperItem
        """
        logging.info(f"Parsing {response.url}")
        item = ProductItem()

        item["extraction_date"] = dt.datetime.now()
        item["shop_name"] = "shop1"
        item["gtin"] = response.xpath('div[@class="product_class]/p/text()').extract()
        item["product_name"] = response.xpath('div[@class="product_class]/p/text()').extract()
        item["price"] = response.css('.product_class::text').extract()
        item["unit"] = response.css('.product_class::text').extract()
        item["url"] = response.url

        yield item
