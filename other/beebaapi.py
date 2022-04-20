# -*- coding:utf8 -*-
import requests,json,time,requests,unittest
from beebashop_API.common.common import url,timestamp,Authorization

headers_012 = {'Authorization': Authorization, 'Beeba-Timestamp':timestamp, 'Beeba-Sign': ''}

url005 = url + '/api/v1/user-coin-logs'
headers01 = {'Authorization': Authorization,
             'Beeba-Timestamp': timestamp,
             'Beeba-Sign': ''}
data_b = {'from_name': 'rechage',
          'type_name': 'balance',
          'created_time_start': '2018-08-20',
          'created_time_end': '2018-08-31'}
r = requests.get(url=url005, headers=headers01, data=data_b)
result = r.json()
print(result)





