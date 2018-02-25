import os
import csv

class ArticleCSVPipeline(object):
    def open_spider(self, spider):
        fieldnames = ['id', 'url', 'headline', 'publish_date', 'author']
        if 'out.csv' in os.listdir('.'):
            os.remove('out.csv')
        self.file = open('out.csv', 'w', newline='')
        self.writer = csv.DictWriter(self.file, delimiter=',', fieldnames=fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        line = dict(item)
        self.writer.writerow(line)

    def close_spider(self, spider):
        self.file.close()