import redis
from scrapy import Request
from epro2.settings import redis_db,redis_host,redis_port
from epro2.settings import pages

def conredis():
    pool=redis.ConnectionPool(host=redis_host,port=redis_port,db=redis_db)
    r=redis.Redis(connection_pool=pool)
    return r
def conmysql():
    pass

#lightnovel.cn

def genlnurl(type,i):
    i=str(i)
    if type=='news':
        url='https://www.lightnovel.cn/forum-96-'+i+'.html'
    elif type=='novel':
        url = 'https://www.lightnovel.cn/forum-4-' + i + '.html'
    elif type=='latestnovel':
        url = 'https://www.lightnovel.cn/forum-173-' + i + '.html'
    else:
        url=''
    return url

def  urltoredis(r,infoclass,urlclass):
    # infoclass=('news','latestnovel','novel')
    # urlclass='lightnovel'
    for m in infoclass:
        print('m=', m)
        for n in range(1, pages + 1):
            url = genlnurl(m, n)
            print('url=',url)
            r.lpush(urlclass, url)


def redistostr(r,urlclass):
    print('--------------URLCLASS--', urlclass)
    kv = (r.brpop(urlclass, timeout=0))
    url = kv[1].decode()
    print('------redistostr----------', url)
    return url
def urlfromredis(r,urlclass):
    list=[]
    url=redistostr(r,urlclass)
    while (url!='over'):
        list.append(url)
    return list

#     print('--------urlfromredis--------',url)
#
#     #     url = redistostr(r, urlclass)
#     #     print('damn  damn')
#     print('sdfsdfsdfsdfsadf')




