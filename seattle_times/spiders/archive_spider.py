import scrapy

from seattle_times.items import Article


class ArchiveSpider(scrapy.Spider):
    name = "archives"

    def __init__(self):
        self.base_url = 'https://www.seattletimes.com/seattle-news/politics/page/'

    def start_requests(self):
        urls = [self.base_url + str(i) + "/" for i in range(1, 10)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        articles = response.selector.css('.subsection').css('article.results-story').css("article")
        ids = [article.xpath("@id").extract_first().replace("post-", "") for article in articles]
        urls = [article.css("h3.results-story-title").css("a::attr(href)").extract_first() for article in articles]
        titles = [article.css("h3.results-story-title").css("a::text").extract_first() for article in articles]
        publish_dates = [article.css("div").css("time::attr(datetime)").extract_first() for article in articles]

        for i in range(len(ids)):
            article = Article(id = ids[i], url=urls[i], headline=titles[i], publish_date=publish_dates[i])
            request = scrapy.Request(urls[i], callback=self.parse_article)
            request.meta['item'] = article
            yield request


    def parse_article(self, response):
        item = response.meta['item']
        byline = response.css(".article-byline")
        authors_selectors = byline.css("div.byline-text").css("div.name").css("a::text").extract()
        authors = ", ".join(authors_selectors)
        authors = authors.encode('utf8')
        item['author'] = authors
        yield item