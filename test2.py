from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import re
import json

with open('cookies.txt', 'r') as f:
     cookies=json.loads(f.read())

def fun1(url):
    session=requests.Session()
    headers={
    'Referer':'http://tieba.baidu.com/i/i/forum',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Host':'tieba.baidu.com'
    }
    r=session.get(url,headers=headers,cookies=cookies)
    objk=BeautifulSoup(r.text)
    list=objk.findAll('a',{'href':re.compile("/f\?kw=")})
    return list

def postT(url):
    session=requests.Session()
    headers={
    'Referer':'https://tieba.baidu.com/f?kw=prisonschool&fr=index&fp=0&ie=utf-8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Origin':'https://tieba.baidu.com'
    }
    list=fun1('http://tieba.baidu.com/f/like/mylike?v=1524730911852')
    for x in list:
        datas={
        'ie':'utf-8',
        'kw':x.get_text(),
        'tbs':'f7790c8cd44ef2371524714254'
        }
        r=session.post(url,data=datas,headers=headers,cookies=cookies)
        print(r.json(),x.get_text())
        time.sleep(20)
        # if r.json()['error']!='success': continue

while True:
    try:
        postT('https://tieba.baidu.com/sign/add')
    except BaseException as e:
        continue
    time.sleep(86400)
