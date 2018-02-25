import json


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('site' + '.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        data = dict(item)
        self.file.write(json.dumps(data) + "\n")
        return item