import scrapy

class ArticleListing(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    headline = scrapy.Field()
    publish_date = scrapy.Field()
