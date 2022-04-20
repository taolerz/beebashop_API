# -*- coding:utf-8 -*-

import time,unittest,HTMLTestRunner,requests
import json,allure
from beebashop_API.common.MySQL_telent import TX
from beebashop_API.common.common import url,Authorization,timestamp

@allure.feature('钱包')
class wallet(unittest.TestCase):      #钱包
    def setUP(self):
        pass
    @allure.story('001余额充值')
    def test_wallet0101(self):
        '''001余额充值'''
        url005 = url + '/api/v1/recharges'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data_b = {'amount': '5'}      # 充值金额   单位是分还是元？

        r = requests.post(url=url005 ,headers=headers01 ,data=data_b)
        result=r. json()
        msg= 'ok'
        self.assertEqual(msg, result['errmsg'])

    def test_wallet0102(self):
        '''002充值记录'''
        url005 = url + '/api/v1/recharges'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}

        r = requests.get(url=url005, headers=headers01)
        result = r.json()
        msg = 'ok'
        self.assertEqual(msg, result['errmsg'])

    def test_withdraw0101(self):
        '''提现申请,提现金额不超过提现金额'''
        url005 = url + '/api/v1/cashes'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data_b = {'amount': '6',}
        r = requests.post(url=url005 ,headers=headers01 ,data=data_b)
        result=r. json()
        msg= '申请成功'
        self.assertEqual(msg, result['errmsg'])

    def test_withdraw0102(self):
        '''提现申请,提现金额超过提现金额'''
        url005 = url + '/api/v1/cashes'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data_b = {'amount': '9999999999'}
        r = requests.post(url=url005 ,headers=headers01 ,data=data_b)
        result=r. json()
        msg= '余额不足'
        self.assertEqual(msg, result['errmsg'])

    def test_withdrawclean0101(self):
        '''取消提现申请,存在的提现订单,并且状态为待支付；已取消的订单会报“提现单状态错误”'''
        url005 = url + '/api/v1/cashes/cancel'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data_b = {'cash_id': TX}

        r = requests.post(url=url005 ,headers=headers01 ,data=data_b)
        result=r. json()
        msg= '取消提现申请成功'
        self.assertEqual(msg, result['errmsg'])

    def test_withdrawclean0102(self):
        '''取消提现申请,不存在的提现订单'''
        url005 = url + '/api/v1/cashes/cancel'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data_b = {'cash_id': '1000'}

        r = requests.post(url=url005 ,headers=headers01 ,data=data_b)
        result=r.json()
        msg= '您没有此条提现记录'
        self.assertEqual(msg, result['errmsg'])

    def test_withdraw0103(self):
        '''提现记录'''
        url005 = url + '/api/v1/cashes'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}

        r = requests.get(url=url005 ,headers=headers01 )
        result=r. json()
        msg= 'ok'
        self.assertEqual(msg, result['errmsg'])

    def test_withdraw0104(self):        #
        '''流水记录搜索'''
        url005 = url + '/api/v1/user-coin-logs'
        headers01 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data_b = {'from_name': 'rechage',
                  'type_name': 'balance',
                  'created_time_start': '2018-08-20',
                  'created_time_end': '2018-09-14'}
        r = requests.get(url=url005 ,headers=headers01,data=data_b )
        result=r. json()
        msg= 'ok'
        self.assertEqual(msg, result['errmsg'])

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()

