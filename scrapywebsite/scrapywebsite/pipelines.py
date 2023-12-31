# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Xác định nơi lưu trữ dữ liệu quét về lưu bằng database
from itemadapter import ItemAdapter
# data scraper -> item containers -> json/csv files
# data scraper -> item containers -> pipelines -> SQL/Mongo Database
import mysql.connector


class ScrapywebsitePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Abcd123424022001',
            database="firstCrawl"
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS firstCrawl_tb""")
        self.curr.execute("""create table firstCrawl_tb(
    title text,
    author text,
    tag text
    )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into firstCrawl_tb values (%s,%s,%s)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
