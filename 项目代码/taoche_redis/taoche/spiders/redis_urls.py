import redis
from .city import CAR_CODE_LIST,CITY_CODE
#创建一个redis连接
redis_ = redis.Redis()
print(1)
for city in CITY_CODE:
    for car in CAR_CODE_LIST:
        base_url = f'https://{city}.taoche.com/{car}/?page=1'
        redis_.lpush('taoche:start_urls',base_url)


#从机不负责主机url任务列表初始化 list 队列 从机拷贝过去的 需要注释上面代码