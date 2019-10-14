import os
import pymysql
from lib.utility.path import DATA_PATH
from lib.zone.city import *
from lib.utility.date import *
from lib.utility.version import PYTHON_3
from lib.spider.base_spider import SPIDER_NAME
from config.db import *

import records

cursor = conn.cursor()
def insertXiaoquInfo(city,district,area,xiaoqu):
    sql = 'insert into xiaoqu_info(city,district,area,xiaoqu) values(%s,%s,%s,%s)'
    cursor.execute(sql, [city, district, area, xiaoqu])
    conn.commit()
    lastrowid = cursor.lastrowid
    return lastrowid


def getXiaoquInfoId(city, district, area, xiaoqu):
    xiaoqu_info_id = xiaoqu_info_dict.get(district + '_' + area + '_' + xiaoqu)
    if xiaoqu_info_id != None:
        # print([district,area,xiaoqu],'存在')
        return  xiaoqu_info_id
    else:
        print([district, area, xiaoqu], '不存在,新增')
        xiaoqu_info_id = insertXiaoquInfo(city, district, area, xiaoqu)
        xiaoqu_info_dict[district + '_' + area + '_' + xiaoqu] = xiaoqu_info_id
        return xiaoqu_info_id


def getXiaoquInfo():
    print('初始化小区数据')
    rows = db.query('select id,district,area,xiaoqu from xiaoqu_info')
    for index,row in enumerate(rows):
        #print('开始处理第:',index,'行')
        xiaoqu_info_dict[row.district+'_'+row.area+'_'+row.xiaoqu] = row.id
    print('初始化小区成功-------------------,共',len(xiaoqu_info_dict),'行')
    


def saveToXiaoquPrice(items):
    db.bulk_query(
        "insert xiaoqu_price(xiaoqu_info_id, date,city,district,area,xiaoqu,price,sale) values(:xiaoqu_info_id, :date,:city,:district,:area,:xiaoqu,:price,:sale)",
        items)


if __name__ == '__main__':
    collection = None
    workbook = None
    csv_file = None
    datas = list()

    xiaoqu_info_dict = {}
    getXiaoquInfo()
    xiaoqu_price_items = []

    city = get_city()
    date = get_date_string()
    city_ch = get_chinese_city(city)
    csv_dir = "{0}/{1}/xiaoqu/{2}/{3}".format(DATA_PATH, SPIDER_NAME, city, date)
    files = list()
 
    if not os.path.exists(csv_dir):
        print("{0} does not exist.".format(csv_dir))
        print("Please run 'python xiaoqu.py' firstly.")
        print("Bye.")
        exit(0)
    else:
        print('OK, start to process ' + get_chinese_city(city))
    for csv in os.listdir(csv_dir):
        data_csv = csv_dir + "/" + csv
        # print(data_csv)
        files.append(data_csv)
    # 清理数据
    count = 0
    row = 0
    col = 0
    for csv in files:
        xiaoqu_price_items = []
        with open(csv, 'r',encoding='utf8') as f:
            for line in f:
                count += 1
                text = line.strip()
                try:
                    # 如果小区名里面没有逗号，那么总共是6项
                    if text.count(',') == 5:
                        date, district, area, xiaoqu, price, sale = text.split(',')
                    elif text.count(',') < 5:
                        continue
                    else:
                        fields = text.split(',')
                        date = fields[0]
                        district = fields[1]
                        area = fields[2]
                        xiaoqu = ','.join(fields[3:-2])
                        price = fields[-2]
                        sale = fields[-1]
                except Exception as e:
                    print(text)
                    print(e)
                    continue

                sale = sale.replace(r'套在售二手房', '')
                price = price.replace(r'暂无', '0')
                price = price.replace(r'元/m2', '')
                price = int(price)
                sale = int(sale)
                #print("{0} {1} {2} {3} {4} {5}".format(date, district, area, xiaoqu, price, sale))
                

                xiaoqu_info_id = getXiaoquInfoId(city,district,area,xiaoqu)
                xiaoqu_price_items.append({
                    'xiaoqu_info_id':xiaoqu_info_id,
                    'date':date,
                    'city':city_ch,
                    'district':district,
                    'area':area,
                    'xiaoqu':xiaoqu,
                    'price':price,
                    'sale':sale
                })
                
        print('[%s,%s,%s]新增了:%s行'%(city_ch,district,area,len(xiaoqu_price_items)))
        if len(xiaoqu_price_items) > 0:
            saveToXiaoquPrice(xiaoqu_price_items)


        


                





