# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XiaoshuoPipeline:
    def open_spider(self,spider):
        self.filename = open('xiaoshuo.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # info = item['title'] + '\n' + item['content'] + '\n'
        info = item['title'] + '\n'
        self.filename.write(info)
        # 关于文件流的问题：写文件时，python会把内容先临时存放在内存中，达到一定的空间之后再写道文件中。因此文件内容比较少时，有可能不能写道文件中，此时为了避免
        # 这种情况，可以使用self.filename.flush()来手工写道文件中，避免上述问题的发生。不过我试了一下，好像不管内容多少，python都可以
        # 写入文件
        # self.filename.flush()
        return item

    def close_spider(self,spider):
        self.filename.close()
