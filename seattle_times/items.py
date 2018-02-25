import scrapy

class Article(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    headline = scrapy.Field()
    publish_date = scrapy.Field()

