# -*- coding:utf8 -*-
import urllib,requests
import re
import json
from collections import OrderedDict
import time,requests,unittest,HTMLTestRunner
from beebashop_API.common.common import url,Authorization,timestamp

url = url+'/api/v1/users/auth'

headers_a = {'Authorization':Authorization,'Beeba-Timestamp':timestamp,'Beeba-Sign':''}

data_b = {'idcard':'445281199308281888',
          'pic_back':'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',
          'pic_front':'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',
          'pic_hand':'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png'}

r = requests.post(url=url,headers=headers_a,data=data_b)
print(r)
print(r.status_code)
print(r.text)
print(r.json())





