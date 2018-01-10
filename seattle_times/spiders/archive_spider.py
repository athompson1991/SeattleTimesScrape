import scrapy

class ArchiveSpider(scrapy.Spider):
    name = "archives"

    def __init__(self):
        self.base_url = 'https://www.seattletimes.com/seattle-news/politics/page/'

    def start_requests(self):
        urls = [self.base_url + str(i) + "/" for i in range(10)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_number = response.url.replace(self.base_url, "").replace("/", "")
        article_listings = response.selector.css('.subsection').css('article.results-story')
        ids = article_listings.xpath("@id").extract()
        urls = article_listings.xpath("//article").css("h3.results-story-title").css("a::attr(href)").extract()
        titles = article_listings.css("h3.results-story-title").css("a::text").extract()
        publish_dates = article_listings.xpath("//article//div//time/@datetime").extract()
        self.log('scraped page: %s' % page_number)
        yield {'ids': ids, 'urls': urls, 'titles': titles, 'publish_dates': publish_dates}