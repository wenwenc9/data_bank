import hashlib
CUSTOM_SETTINGS = {
    #robotes协议
    'ROBOTSTXT_OBEY': False,
    #请求头
    'DEFAULT_REQUEST_HEADERS' : {
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en',
            # 'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        },
    #下载中间件
    # 'DOWNLOADER_MIDDLEWARES' : {
    #    'sh_company.user_agent_middle.User_Agent_Middle': 543,
    # },

    #pipelines
    'ITEM_PIPELINES' :{
       'taoche.pipelines.MongoPipeline': 300,
    },
    #数据库的url
    'MONGO_URI' :'localhost',
    #数据的名字
    'MONGO_DATABASE' :'taoche',
}
def get_md5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()

def update_to_mongo(db,collectionName,id,url,item):
    '''

    :param db: db引用
    :param collectionNmae: 集合名
    :param id: item的更新字典
    :param url: 生成id字段
    :param item:

    :return:
    '''

    if url:
        item[id] = get_md5(item[url])
        db[collectionName].update({id:item[id]},{'$set':dict(item)},True)
        print(item)
    else:
        db[collectionName].update({id: item[id]}, {'$set': dict(item)}, True)
        print(item)

def add_page(m):
    page_num = str(int(m.group(1))+1)
    return '?page='+page_num