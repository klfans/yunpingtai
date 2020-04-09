import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15855395889509'


def get_sign():
    return 'd8416f78b54601efd1bed7a202bee31c'


def get_ts():
    return '1585539588950'


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