# import multiprocessing
# #import threading
# #import os
# from scrapy import cmdline
# #from concurrent.futures import ThreadPoolExecutor
#
# def action(number):
#     print('start price_list crawl', str(number))
#     cmdline.execute('scrapy crawl price_list'.split())
#
# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=4) as pool:
#         # 使用线程执行map计算
#         # 后面元组有3个元素，因此程序启动3条进程来执行action函数
#         results = pool.map(action, (1, 2, 3))
#         print('--------------')

from scrapy.crawler import CrawlerProcess
from mofcom.spiders.list import ListSpider as price_list_spider
from mofcom.spiders.product_screen import ProductScreenSpider as product_screen_spider
from scrapy.utils.project import get_project_settings

def start_spider():
    try:
        process = CrawlerProcess(get_project_settings())
        process.crawl(price_list_spider)
        process.crawl(price_list_spider)
        process.crawl(price_list_spider)
        process.crawl(price_list_spider)
        process.start()
    except Exception as e:
        print('---出现错误---', e)

if __name__ == '__main__':
    start_spider()


