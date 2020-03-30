import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
from_data={
    'i':'我和你',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15855395889509',
    'sign':'d8416f78b54601efd1bed7a202bee31c',
    'ts':'1585539588950',
    'bv':'70244e0061db49a9ee62d341c5fed82a',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
response=requests.post(url,from_data)
print(response.text)