import time,unittest,HTMLTestRunner,requests,json
from fenlaishop.common.common import timestamp,userId,url

url =  r'http://app.51zheli.com'
userId = '2c928ae96ca8ae53016ca9098ffc0027'

headers001={'appVersion': '2.9.1',
           'deviceId': '866413032471383',
           'operationTime': timestamp,
           'osType': 'android',
           'osVersion': '9',
           'token': '5da0a83de4e770a980ef850a2df2deea',
            'sign': 'fe887521f3bf1d947b272eb89365014665d1f457'
           }
url07 = url + '/cart/save'
data01 = {'count': '1',
          'productId': '110150',
          'skuId': '19503',
          'storeId': '10',
          'userId': '2c928ae96ca8ae53016ca9098ffc0027'
          }
r = requests.post(url=url07, headers=headers001, data=data01)
result = r.json()
#msg = 'success'
print(result)
#assertEqual(msg, result['msg'])
