# -*- coding:utf-8 -*-

import time,unittest,HTMLTestRunner,requests
import json
import requests,allure
from beebashop_API.common.common import url,Authorization,timestamp
@allure.feature('公共部分测试')
class beeba_wechatskip(unittest.TestCase):
    def setUp(self):
        pass

    @allure.story('微信跳转验证')
    def test_wechat_skip(self):
        '''微信跳转验证'''
        url_01 = url+'/api/v1/site/wx-url'
        headers01 = {'Beeba-Timestamp':timestamp,
                     'Beeba-Sign':''}
        r=requests.get(url=url_01,headers=headers01)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    @allure.story('获取文章的列表验证')
    def test_get_list(self):
        '''获取文章的列表验证'''
        url_02 = url+'/api/v1/articles?type=news'
        data_a = {'Authorization':Authorization}
        r=requests.get(url=url_02,headers=data_a)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    @allure.story('获取单独文章内容验证')
    def test_get_text(self):
        '''获取单独文章内容验证'''
        url_02 = url+'/api/v1/articles/114'
        data_03 = {'Authorization':Authorization}
        r=requests.get(url=url_02,headers=data_03)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    @allure.story('上传图片验证')
    def test_Upload_picture(self):  #上传图片
        '''上传图片验证'''
        url_03 = url+'/api/v1/upload'
        data_03 = {'Authorization':Authorization,
                   'Beeba-Timestamp':timestamp,
                   'Content-Type':'application/x-www-form-urlencoded',
                   'Beeba-Sign': ''}  # 图片的base64
        data_004 = {'img': 'data:image/jpeg;base64,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',
                    'type': 'avatar', }  # 类型 avatar 头像上传  auth 实名认证
        r=requests.post(url=url_03,headers=data_03,data=data_004)
        result=r.json()
        msg='上传成功'
        self.assertEqual(msg,result['errmsg'])

    def test_homepage(self):
        '''首页内容'''
        url_03 = url+'/api/v1/user-agents/children'
        data_03 = {'Authorization':Authorization}
        r=requests.get(url=url_03,headers=data_03)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_homepage(self):
        '''省市区三级联动'''
        url_04 = url+'/api/v1/areas?id=19'
        data_04 = {'Authorization':Authorization}
        r=requests.get(url=url_04,headers=data_04)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_homepage(self):
        '''提现回调'''
        url_04 = url+'/api/v1/wxpay/refund-notify'
        data_04 = {'Authorization':Authorization,
                   'Beeba-Timestamp':timestamp,
                   'Content-Type':'application/x-www-form-urlencoded',
                   'Beeba-Sign':''}
        r=requests.post(url=url_04,headers=data_04)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_homepage(self):
        '''支付回调'''
        url_05 = url+'/api/v1/wxpay/pay-notify'
        headers_05 = {'Authorization':Authorization,
                   'Beeba-Timestamp':timestamp,
                   'Content-Type':'application/x-www-form-urlencoded',
                   'Beeba-Sign':''}
        data_05 = {'out_trade_no':'84589558067706005',
                   'transaction_id':'111',
                   'total_fee':'111',
                   'attach':'order',
                   'result_code':'SUCCESS'}
        r=requests.post(url=url_05,headers=headers_05,data=data_05)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()

