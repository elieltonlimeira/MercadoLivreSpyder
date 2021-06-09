import scrapy


class MlivrescrapyItem(scrapy.Item):
    
    nome = scrapy.Field()
    preco = scrapy.Field()
    pass
