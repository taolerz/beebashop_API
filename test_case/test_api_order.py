import time,unittest,requests
import json,allure
from beebashop_API.common.common import url,Authorization,timestamp
from beebashop_API.common.MySQL_telent import DDXQ,QXDD,WCDD,XJDD,XJYF1

@allure.feature('我的订单和下级订单')
class beeba_team(unittest.TestCase):
    def setUp(self):
        pass

    def test_myorder01(self):
        '''我的订单'''
        url_023 = url+'/api/v1/orders'
        headers23 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_023,headers=headers23)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder02(self):
        '''我的订单详情。没有订单会报null'''
        url_024 = url+'/api/v1/orders/'+DDXQ
        headers24 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_024,headers=headers24)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder03(self):
        '''取消订单。不存在的订单会报null,未支付的订单才能取消'''
        url_025 = url+'/api/v1/orders/cancel'
        headers25 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data25 = {'id':QXDD}
        r=requests.post(url=url_025,headers=headers25,data=data25)
        result=r.json()
        msg='操作成功'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder04(self):
        '''完成订单。不存在的订单会报null；订单状态为已发货才可以完成订单'''
        url_026 = url+'/api/v1/orders/finish'
        headers26 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        #cursor.execute("UPDATE bb_order SET status='30' WHERE (id='69')")

        data26 = {'area_info': '广东省深圳市南山区',  # 省市区
                  'truename': '比巴',  # 联系人
                  'phone': '18688118811',  # 电话
                  'address': '科技生态园6栋9层',  # 详细地址
                  'is_default':'1',
                  'id':WCDD}
        r=requests.post(url=url_026,headers=headers26,data=data26)
        result=r.json()
        msg='操作成功'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder05(self):
        '''我的下级订单'''
        url_027 = url+'/api/v1/order-agents'
        headers27 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_027,headers=headers27)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder06(self):
        '''我的下级待付款订单详情。没有订单或订单id错误会报null'''
        url_028 = url+'/api/v1/order-agents/'+XJDD
        headers28 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_028,headers=headers28)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder07(self):
        '''取消下级待付款订单。不存在的订单会报null'''
        url_029 = url+'/api/v1/orders/cancel'
        headers29 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data29 = {'id':XJDD}
        r=requests.post(url=url_029,headers=headers29,data=data29)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder08(self):
        '''下级订单发货'''
        url_030 = url+'/api/v1/order-agents/send'
        headers30 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data30 = {'area_info': '广东省深圳市南山区',  # 省市区
                  'truename': '比巴',  # 联系人
                  'phone': '18688118811',  # 电话
                  'address': '科技生态园6栋9层',  # 详细地址
                  'is_default':'1',
                  'id':XJYF}
        r=requests.post(url=url_030,headers=headers30,data=data30)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_myorder09(self):
        '''下级订单转发'''
        url_031 = url+'/api/v1/order-agents/forward'
        headers31 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data31 = {'area_info': '广东省深圳市南山区',  # 省市区
                  'truename': '比巴',  # 联系人
                  'phone': '18688118811',  # 电话
                  'address': '科技生态园6栋9层',  # 详细地址
                  'is_default':'1',
                  'id':XJYF1}
        r=requests.post(url=url_031,headers=headers31,data=data31)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()
