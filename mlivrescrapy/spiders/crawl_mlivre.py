import scrapy
from ..items import MlivrescrapyItem

class CrawlMlivreSpider(scrapy.Spider):
    name = 'crawl_mlivre'
    start_urls = ['https://lista.mercadolivre.com.br/smartphone']

    def parse(self, response):
        item = MlivrescrapyItem()
        
        item['nome'] = response.css('.ui-search-item__title::text').getall()
        item['preco'] = response.css('.ui-search-price--size-medium .ui-search-price__second-line .price-tag-fraction::text').getall()
        yield item
