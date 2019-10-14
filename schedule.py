from lib.spider.xiaoqu_spider import *
import xiaoqu_to_mysql

if __name__ == "__main__":
    spider = XiaoQuBaseSpider(SPIDER_NAME)
    spider.start()

    xiaoqu_to_mysql.start()

