# -*- coding:utf-8 -*-

import time,unittest,requests,allure
import json
from beebashop_API.common.common import timestamp,Authorization,url

url2 = url+'/api/v1/users/send'
headers_a = {'Authorization': Authorization, 'Beeba-Timestamp':timestamp, 'Beeba-Sign': ''}
@allure.feature('发送手机验证码')
class user_tel01(unittest.TestCase):
    def setUP(self):
        pass
    def test_sendmsg0101(self):
        '''001验证已绑定的手机号码'''
        data_b = {'mobile':'18688110215'}
        r = requests.post(url=url2,headers=headers_a,data=data_b)
        result=r.json()
        msg='该手机已被绑定'
        self.assertEqual(msg,result['errmsg'])

    def test_sendmsg0102(self):
        '''002验证未绑定的手机号码'''
        data_c = {'mobile':'18688110216'}
        r = requests.post(url=url2,headers=headers_a,data=data_c)
        result=r.json()
        msg='验证码发送成功'
        self.assertEqual(msg,result['errmsg'])

    def test_sendmsg0103(self):
        '''003验证手机号码为空的情况'''
        data_c = {'mobile':''}
        r = requests.post(url=url2,headers=headers_a,data=data_c)
        result=r.json()
        msg='手机号不能为空。'
        self.assertEqual(msg,result['errmsg'])

    def test_sendmsg0104(self):
        '''004验证非手机号码的情况'''
        data_c = {'mobile':'00000000'}
        r = requests.post(url=url2,headers=headers_a,data=data_c)
        result=r.json()
        msg='手机号是无效的。'
        self.assertEqual(msg,result['errmsg'])

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()


