import scrapy

class ArchiveSpider(scrapy.Spider):
    name = "archives"

    def start_requests(self):
        urls = [
            'https://www.seattletimes.com/seattle-news/politics/page/1/'
            'https://www.seattletimes.com/seattle-news/politics/page/2/'
            'https://www.seattletimes.com/seattle-news/politics/page/3/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'archive-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)