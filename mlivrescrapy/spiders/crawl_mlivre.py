import scrapy
from ..items import MlivrescrapyItem

class CrawlMlivreSpider(scrapy.Spider):
    name = 'crawl_mlivre'
    start_urls = ['https://lista.mercadolivre.com.br/smartphone']

    def parse(self, response):
        item = MlivrescrapyItem()
        products = response.css('li.ui-search-layout__item')
       
        for p in products:
            item['nome'] = p.css('.ui-search-item__title::text').get()
            item['preco'] = p.css('.ui-search-price--size-medium .ui-search-price__second-line .price-tag-fraction::text').get()
            yield item
