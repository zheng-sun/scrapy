# from scrapy import cmdline
#
# cmdline.execute('scrapy crawl price_list'.split())

from mofcom.Models.GetData import GetData

product_list = GetData().getProduct()
print(product_list)