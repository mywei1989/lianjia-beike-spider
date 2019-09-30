import pymysql
import records

pymysql.install_as_MySQLdb()
db = records.Database('mysql://root:root@8.8.8.8/aaa?charset=utf8', encoding='utf-8')
conn = pymysql.connect(
    host='8.8.8.8',
    port=3306,
    user='root',
    password='88888',
    database='fangjia',
    charset="utf8"
)