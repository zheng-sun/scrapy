from mofcom.Models.GetData import GetData
from mofcom.Models.Add import Add
import datetime
from dateutil.relativedelta import relativedelta
import time
import logging

# 写入日志
def get_logger():
    log_dir = 'mofcom/logs/main.log'
    fh = logging.FileHandler(log_dir, encoding='utf-8') #创建一个文件流并设置编码utf8
    logger = logging.getLogger() #获得一个logger对象，默认是root
    logger.setLevel(logging.DEBUG)  #设置最低等级debug
    fm = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")  #设置日志格式
    logger.addHandler(fh) #把文件流添加进来，流向写入到文件
    fh.setFormatter(fm) #把文件流添加写入格式
    return logger

logger = get_logger()

# 循环获取需要读取的链接
def handles_region_product():
    data_list = []
    product_list = GetData().getProduct()
    # print('product_list:')
    # print(product_list)
    # print(len(product_list))
    region_list = GetData().getRegion()
    # print('region_list:')
    # print(region_list)
    # print(len(region_list))
    if product_list is not None:
        for product_data in product_list:
            if region_list is not None:
                for region_data in region_list:
                    data = {}
                    data['category_id'] = product_data['category_id']
                    data['product_id'] = product_data['product_id']
                    data['region_id'] = region_data['region_id']
                    data_list.append(data)
    return data_list

# 循环开始时间到今天的日期
def while_datetime(start_date, end_date):
    datestart = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    # 时间间隔
    month_differ = abs((datestart.year - dateend.year) * 12 + (datestart.month - dateend.month) * 1)

    date_list = []
    if month_differ > 1:
        while datestart < dateend:
            date_l = {}
            date_l['start_date'] = datestart.strftime('%Y-%m-%d')
            datestart = datestart + relativedelta(months=3)
            date_l['end_date'] = datestart.strftime('%Y-%m-%d')
            date_list.append(date_l)
    else:
        while datestart < dateend:
            date_l = {}
            date_l['start_date'] = datestart.strftime('%Y-%m-%d')
            datestart += datetime.timedelta(days=1)
            date_l['end_date'] = datestart.strftime('%Y-%m-%d')
            date_list.append(date_l)
    return date_list

def main():
    start_date = '2014-01-01'
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    region_product_list = handles_region_product()
    while_date = while_datetime(start_date, end_date)
    while len(region_product_list) > 0:
        product = region_product_list.pop()
        for date in while_date:
            print('开始生成链接 product_id: %s , category_id: %s , region_id: %s', product['product_id'], product['category_id'], product['region_id'])
            logger.info('开始生成链接 product_id: %s , category_id: %s , region_id: %s', product['product_id'], product['category_id'], product['region_id'])

            item = {}
            item['spider_name'] = 'price_list'
            item['url'] = 'http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index='+str(product['category_id'])+'&craft_index='+str(product['product_id'])+'&par_p_index='+str(product['region_id'])+'&startTime='+str(date['start_date'])+'&endTime='+str(date['end_date'])
            item['code'] = '0'

            getOne = GetData().getReptileByUrl([item['url']])
            if getOne == 0:
                logger.info("生成链接: %s ", item['url'])
                Add().insertReptile(item)
        logger.info('暂停5秒')
        time.sleep(5)
    logger.info('链接生成完成,一共生成')

if __name__ == "__main__":
    main()