# -*- coding:utf-8 -*-
import time,unittest,requests,json,allure
from beebashop_API.common.common import timestamp,url,Authorization
from beebashop_API.common.MySQL_telent import NN

headers_012 = {'Authorization': Authorization, 'Beeba-Timestamp':timestamp, 'Beeba-Sign': ''}

@allure.feature('商城部分')
class shopping(unittest.TestCase):
    def setUP(self):
        pass

    def test_goods_list(self):
        '''001验证商品列表'''
        url012 = url + '/api/v1/goods'
        r = requests.get(url=url012,headers=headers_012)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_goods_details(self):
        '''002验证商品详情'''
        url013 = url + '/api/v1/goods/1'
        r = requests.get(url=url013,headers=headers_012)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_carts_list(self):
        '''003购物车列表'''
        url014 = url + '/api/v1/carts'
        r = requests.get(url=url014,headers=headers_012)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_carts_count(self):
        '''004购物车数量'''
        url015 = url + '/api/v1/carts/count'
        r = requests.get(url=url015,headers=headers_012)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_add_carts01(self):
        '''输入存在的商品，商品数量为1，添加购物车'''
        url016 = url + '/api/v1/carts'
        data016 = {'goods_id':'1',       #商品ID
                   'quantity':'1',       #商品数量 -1减少数量 1 增加数量
                   'spec_id':'0'}        #规格ID
        r = requests.post(url=url016,headers=headers_012,data=data016)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_add_carts02(self):
        '''输入存在的商品，商品数量为特殊字符，添加购物车'''
        url016 = url + '/api/v1/carts'
        data016 = {'goods_id':'1',       #商品ID
                   'quantity':'@',       #商品数量 -1减少数量 1 增加数量
                   'spec_id':'0'}        #规格ID
        r = requests.post(url=url016,headers=headers_012,data=data016)
        result=r.json()
        msg='数量必须是整数。'           #应该为正整数
        self.assertEqual(msg,result['errmsg'])

    def test_add_carts03(self):
        '''输入存在的商品，商品数量为负数，添加购物车'''
        url016 = url + '/api/v1/carts'
        data016 = {'goods_id':'1',       #商品ID
                   'quantity':'-5。',       #商品数量 -1减少数量 1 增加数量
                   'spec_id':'0'}        #规格ID
        r = requests.post(url=url016,headers=headers_012,data=data016)
        result=r.json()
        msg='数量必须是整数。'
        self.assertEqual(msg,result['errmsg'])

    def test_add_carts04(self):
        '''输入不存在的商品ID，商品数量为1，添加购物车'''
        url016 = url + '/api/v1/carts'
        data016 = {'goods_id':'6',       #商品ID
                   'quantity':'1',       #商品数量 -1减少数量 1 增加数量
                   'spec_id':'0'}        #规格ID
        r = requests.post(url=url016,headers=headers_012,data=data016)
        result=r.json()
        msg='商品不存在或已下架'
        self.assertEqual(msg,result['errmsg'])

# 清空购物车接口取消
#     @allure.story('006清空购物车')
#     def test_clear_carts01(self):
#         '''购物车列表存在添加的商品时，才会用例执行成功，为空时执行失败'''
#         url017 = url + '//api/v1/carts/clear'
#         r = requests.delete(url=url017,headers=headers_012)
#         result=r.json()
#         msg='清除成功'
#         self.assertEqual(msg,result['errmsg'])
#
#     def test_clear_carts02(self):
#         '''当购物车为空的情况下验证'''
#         url017 = url + '//api/v1/carts/clear'
#         r = requests.delete(url=url017,headers=headers_012)
#         result=r.json()
#         msg='清除失败'
#         self.assertEqual(msg,result['errmsg'])

    def test_del_carts01(self):
        '''删除购物车不存在的单个商品'''
        url01701 = url + '//api/v1/carts/1'
        headers_101701 = {'Authorization':Authorization}
        r = requests.delete(url=url01701,headers=headers_101701)
        result=r.json()
        msg='资源不存在'
        self.assertEqual(msg,result['errmsg'])

    def test_del_carts02(self):
        '''删除购物车存在的单个商品'''
        url01702 = url + '//api/v1/carts/'+NN
        headers_101702 = {'Authorization':Authorization}
        r = requests.delete(url=url01702,headers=headers_101702)
        result=r.json()
        msg='清除成功'
        self.assertEqual(msg,result['errmsg'])

    def test_stepone(self):
        '''订单购买第一步'''
        url01801 = url + '/api/v1/buy/step1'
        headers_01801 = {'Authorization':Authorization}
        data_01801 = {'cart_id':'2|2',    #格式 id|num,id|num id 商品ID  num 商品数量 1|1 2|2,3|1
                    'ifcart': '0'}       #是否购物车 0 立即购买  1 购物车购买
        r = requests.post(url=url01801,headers=headers_01801,data=data_01801)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_stepone2(self):
        '''订单购买第一步；选用购物车购买'''
        url018 = url + '/api/v1/buy/step1'
        headers_018 = {'Authorization':Authorization}
        data_018 = {'cart_id':'2|2',    #格式 id|num,id|num id 商品ID  num 商品数量 1|1 2|2,3|1
                    'ifcart': '1'}       #是否购物车 0 立即购买  1 购物车购买
        r = requests.post(url=url018,headers=headers_018,data=data_018)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_steptwo(self):
        '''订单购买第二步'''
        url019 = url + '/api/v1/buy/step2'
        headers_019 = {'Authorization':Authorization}
        data_019 = {'cart_id':'2|2',    #
                    'ifcart': '0',
                    'address_id':'15',
                    'msg': '1',
                    'pay_type': 'pdpay',
                    'type': '1'}       #
        r = requests.post(url=url019,headers=headers_019,data=data_019)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_orderpay(self):
        '''获取订单支付信息'''
        url020 = url + '/api/v1/orders/pay'
        headers_020 = {'Authorization':Authorization}
        data_020 = {'id':'65'}
        r = requests.post(url=url020,headers=headers_020,data=data_020)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()


