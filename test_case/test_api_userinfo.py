# -*- coding:utf-8 -*-

import time,unittest,HTMLTestRunner,requests
import json
import requests,allure
from beebashop_API.common.common import ti,url,timestamp,Authorization

@allure.feature('用户信息')
class beeba_wechatskip(unittest.TestCase):
    def setUp(self):
        pass
    @allure.story('用户信息验证')
    def test_userinfo(self):
        '''查看自己的用户信息'''
        url_02 = url+'/api/v1/users/6'
        send_data = {'Authorization':Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign':''}
        r=requests.get(url=url_02,headers=send_data)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_invitation(self):
        '''邀请海报'''
        url_02 = url+'/api/v1/users/invitation'
        send_data = {'Authorization':Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign':''}
        r=requests.get(url=url_02,headers=send_data)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_certificate(self):
        '''授权证书'''
        url_02 = url+'/api/v1/users/certificate'
        send_data = {'Authorization':Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign':''}
        r=requests.get(url=url_02,headers=send_data)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_agent_levels(self):
        '''申请代理 代理升级'''
        url_02 = url+'/api/v1/agent-levels'
        send_data = {'Authorization':Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign':''}
        r=requests.get(url=url_02,headers=send_data)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_apply(self):
        '''申请代理充值'''
        url_02 = url+'/api/v1/recharges/apply'
        headers07 = {'Authorization':Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign':''}
        data_07 = {'agent_id':'6'}
        r=requests.post(url=url_02,headers=headers07,data=data_07)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_put_users(self):
        '''信息修改'''
        url_02 = url+'/api/v1/users/6'
        headers07 = {'Authorization':Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign':'',
                     'Content - Type':'application/x-www-form-urlencoded'}
        data_07 = {'nickname':'test',
                   'avatar_url':'http://www.baidu.com.jpg',
                   'sheng_id':'19',
                   'shi_id': '291',
                   'qu_id': '3058',}
        r=requests.put(url=url_02,headers=headers07,data=data_07)
        result=r.json()
        msg='成功修改信息'
        self.assertEqual(msg,result['errmsg'])


    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()

