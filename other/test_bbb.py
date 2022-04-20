# -*- coding:utf8 -*-
import requests,unittest,allure
from beebashop_API.common.MySQL_telent import QXDD
from beebashop_API.common.common import url,Authorization,timestamp

'''取消订单。不存在的订单会报null,未支付的订单才能取消'''
url_025 = url+'/api/v1/orders/cancel'
headers25 = {'Authorization': Authorization,
             'Beeba-Timestamp': timestamp,
             'Beeba-Sign': ''}
data25 = {'id':QXDD}
r=requests.post(url=url_025,headers=headers25,data=data25)
result=r.json()
# msg='操作成功'
# self.assertEqual(msg,result['errmsg'])
print(result)


