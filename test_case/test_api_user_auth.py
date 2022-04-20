# -*- coding:utf-8 -*-

import time,unittest,HTMLTestRunner,requests
import json
import requests,allure
from beebashop_API.common.common import timestamp,Authorization,url

url = url+'/api/v1/users/auth'
headers_a = {'Authorization': Authorization, 'Beeba-Timestamp':timestamp, 'Beeba-Sign': ''}

@allure.feature('实名认证')
class user_auth(unittest.TestCase):      #给未绑定身份信息用户实名认证
    def setUP(self):
        pass
    def test_auth01(self):
        '''001未绑定的身份证号验证实名认证成功'''
        data_b = {'idcard': '445281199308281819',
                  'pic_back': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',  #身份证背面图片
                  'pic_front': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png', #身份证正面图片
                  'pic_hand': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',   #手持身份证图片
                  'true_name':'测试001'}
        r = requests.post(url=url,headers=headers_a,data=data_b)
        result=r.json()
        msg='认证申请成功'  #该身份证已被绑定   异议？user_auth02
        self.assertEqual(msg,result['errmsg'])

    def test_auth02(self):
        '''002已绑定的身份证号验证实名认证成功'''
        data_b = {'idcard': '445281199308281888',
                  'pic_back': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',  #身份证背面图片
                  'pic_front': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png', #身份证正面图片
                  'pic_hand': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',  #手持身份证图片
                  'true_name': '测试001'}

        r = requests.post(url=url,headers=headers_a,data=data_b)
        result=r.json()
        msg='该身份证成功绑定'
        self.assertEqual(msg,result['errmsg'])

    def test_auth03(self):
        '''003验证未上传手持身份证图片'''
        data_b = {'idcard': '445281199308281888',
                  'pic_back': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',
                  'pic_front': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',
                  'pic_hand': '',
                  'true_name': '测试001'}
        r = requests.post(url=url,headers=headers_a,data=data_b)
        result=r.json()
        msg='缺少必需的参数: pic_hand'
        self.assertEqual(msg,result['errmsg'])

    def test_auth04(self):
        '''004验证身份证号码为空'''
        data_b = {'idcard': '',
                  'pic_back': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',
                  'pic_front': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',
                  'pic_hand': 'http://cms.beeba.cn/Uploads/Picture/2018-07-31/5b600b5227448.png',
                  'true_name': '测试001'}

        r = requests.post(url=url,headers=headers_a,data=data_b)
        result=r.json()
        msg='缺少必需的参数: idcard'
        self.assertEqual(msg,result['errmsg'])
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()


