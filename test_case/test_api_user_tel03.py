# -*- coding:utf-8 -*-

import time,unittest,requests,json,allure
from beebashop_API.common.common import timestamp,url,Authorization

url011 = url+'/api/v1/users/bind'
headers_a = {'Authorization': Authorization, 'Beeba-Timestamp':timestamp, 'Beeba-Sign': ''}
@allure.feature('绑定手机')
class user_tel03(unittest.TestCase):
    def setUP(self):
        pass

    # def test_sendmsg0301(self):
    #     '''001验证不输入验证码'''
    #     data_b = {'mobile':'18688110211','code':''}
    #     r = requests.post(url=url011,headers=headers_a,data=data_b)
    #     result=r.json()
    #     msg='缺少必需的参数: code'
    #     self.assertEqual(msg,result['errmsg'])

    # def test_sendmsg0302(self):
    #     '''002验证输入错误的验证码'''
    #     data_c = {'mobile':'18688110216','code':'123456'}
    #     r = requests.post(url=url011,headers=headers_a,data=data_c)
    #     result=r.json()
    #     msg='验证码输入错误,请重新输入'
    #     self.assertEqual(msg,result['errmsg'])

    # def test_sendmsg0303(self):
    #     '''003验证输入正确的验证码'''
    #     data_c = {'mobile':'18688110216','code':'dsfdff'}
    #     r = requests.post(url=url011,headers=headers_a,data=data_c)
    #     result=r.json()
    #     msg='手机号不能为空。'
    #     self.assertEqual(msg,result['errmsg'])

    def test_sendmsg0304(self):
        '''004验证已绑定手机号码'''
        data_b = {'mobile':'18688110215','code':''}
        r = requests.post(url=url011,headers=headers_a,data=data_b)
        result=r.json()
        msg='该手机已被绑定'
        self.assertEqual(msg,result['errmsg'])

    def test_sendmsg0305(self):
        '''005验证手机号码为空'''
        data_b = {'mobile':'','code':'123434'}
        r = requests.post(url=url011,headers=headers_a,data=data_b)
        result=r.json()
        msg='手机号不能为空。'
        self.assertEqual(msg,result['errmsg'])

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()


