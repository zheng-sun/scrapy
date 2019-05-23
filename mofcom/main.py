from mofcom.Models.GetData import GetData
from mofcom.Models.Add import Add
import datetime
from dateutil.relativedelta import relativedelta


data = GetData().getReptile('0', 'price_list')
print(data)
# 循环获取需要读取的链接
# def handles_region_product():
#     data_list = []
#     product_list = GetData().getProduct()
#     region_list = GetData().getRegion()
#     if product_list is not None:
#         for product_data in product_list:
#             if region_list is not None:
#                 for region_data in region_list:
#                     data = {}
#                     data['category_id'] = product_data['category_id']
#                     data['product_id'] = product_data['product_id']
#                     data['region_id'] = region_data['region_id']
#                     data_list.append(data)
#     return data_list
#
# # 循环开始时间到今天的日期
# def while_datetime(start_date, end_date):
#     datestart = datetime.datetime.strptime(start_date, '%Y-%m-%d')
#     dateend = datetime.datetime.strptime(end_date, '%Y-%m-%d')
#     # 时间间隔
#     month_differ = abs((datestart.year - dateend.year) * 12 + (datestart.month - dateend.month) * 1)
#
#     date_list = []
#     if month_differ > 1:
#         while datestart < dateend:
#             date_l = {}
#             date_l['start_date'] = datestart.strftime('%Y-%m-%d')
#             datestart = datestart + relativedelta(months=3)
#             date_l['end_date'] = datestart.strftime('%Y-%m-%d')
#             date_list.append(date_l)
#     else:
#         while datestart < dateend:
#             date_l = {}
#             date_l['start_date'] = datestart.strftime('%Y-%m-%d')
#             datestart += datetime.timedelta(days=1)
#             date_l['end_date'] = datestart.strftime('%Y-%m-%d')
#             date_list.append(date_l)
#     return date_list
#
# def main():
#     start_date = '2014-01-01'
#     end_date = datetime.datetime.now().strftime('%Y-%m-%d')
#     region_product_list = handles_region_product()
#     while_date = while_datetime(start_date, end_date)
#
#     #  循环添加地址
#     for product in region_product_list:
#         for date in while_date:
#             item = {}
#             item['spider_name'] = 'price_list'
#             item['url'] = 'http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index='+str(product['category_id'])+'&craft_index='+str(product['product_id'])+'&par_p_index='+str(product['region_id'])+'&startTime='+str(date['start_date'])+'&endTime='+str(date['end_date'])
#             item['code'] = '0'
#             print(item)
#             Add().insertReptile(item)

# if __name__ == "__main__":
#     main()