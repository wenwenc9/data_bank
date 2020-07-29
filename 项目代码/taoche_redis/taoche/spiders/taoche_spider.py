import re
from scrapy_redis import spiders

import scrapy,socket
from .city import CAR_CODE_LIST,CITY_CODE
from ..my_settings import CUSTOM_SETTINGS,add_page
from ..items import TaocheItem
class TaocheSpiderSpider(spiders.RedisSpider):
    name = 'taoche_spider'
    myaddr = socket.gethostbyname(socket.gethostname())
    # allowed_domains = ['www']
    custom_settings = CUSTOM_SETTINGS
    redis_key = 'taoche:start_urls'
    # start_urls = []
    # for city in CITY_CODE:
    #     for car in CAR_CODE_LIST:
    #         start_urls.append(f'https://{city}.taoche.com/{car}/?page=1')

    def parse(self, response):
        li_list = response.xpath('//ul[@class="gongge_ul"]/li')
        # print(li_list)
        # print(len(self.start_urls))
        if li_list:#开关
            for li in li_list:
                #1、解析
                try:
                    car_title = li.xpath('.//div[@class="gongge_main"]/a/@title').extract_first()
                    car_url = li.xpath('.//div[@class="gongge_main"]/a/@href').extract_first()
                    car_now_price = li.xpath('.//div[@class="price"]/i[1]/text()').extract_first()
                    car_old_price = li.xpath('.//div[@class="price"]/i[2]/text()').extract_first()
                    infos = li.xpath('.//div[@class="gongge_main"]/p/i/text()').extract()
                    car_years = infos[0]
                    car_licheng = infos[1]
                    car_product_area = infos[2].strip()
                    # item = {}
                    item = TaocheItem()

                    item['car_title'] = car_title
                    item['car_now_price'] = car_now_price
                    item['car_old_price'] = car_old_price
                    item['car_years'] = car_years
                    item['car_product_area'] = car_product_area
                    item['car_licheng'] = car_licheng
                    item['ip'] = self.myaddr
                    item['car_url'] = car_url

                    yield item

                except Exception:
                    pass

            # 上面缩小的是每一页解析数据 当每一页解析完毕就到下一页了，执行下面程序
            # 2、请求下一页
            now_url = response.url # 获取url，进行正则匹配修改，使用sub函数
            next_url= re.sub(r'\?page=(\d+)',add_page,now_url)
            # print(now_url,next_url,sep='===\n===')
            yield scrapy.Request(next_url,callback=self.parse,encoding='utf-8')



