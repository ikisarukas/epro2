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
    r.lpush(urlclass,'over')


def redistostr(r,urlclass):
    temp=''
    # print('--------------URLCLASS--', urlclass)
    kv = (r.rpop(urlclass))
    # print('kv====',kv.decode())
    if(kv):
        temp = kv.decode()
    print('------redistostr----------', temp)
    print('type of url is ',type(temp))
    return temp
def urlfromredis(r,urlclass):
    list=[]
    url=redistostr(r,urlclass)
    count=0
    while (url!='over'):
        list.append(url)
        print('count=',count)
        url = redistostr(r, urlclass)
        print('temp url   ------------------',url)
        count+=1
    for i in list:
        print('i  in list  is ',i)
    return list





