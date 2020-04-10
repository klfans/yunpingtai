import requests
import time
import random

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    return  t+s


def get_sign():
    return 'd8416f78b54601efd1bed7a202bee31c'


def get_ts():
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts


from_data={
    'i':'我和你',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv':'70244e0061db49a9ee62d341c5fed82a',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
response=requests.post(url,from_data)
print(response.text)