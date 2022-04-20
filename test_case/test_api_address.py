# -*- coding:utf-8 -*-
import time,unittest,HTMLTestRunner,requests,json,allure
from beebashop_API.common.common import timestamp,url,Authorization
from beebashop_API.common.MySQL_telent import M

headers_a = {'Authorization': Authorization, 'Beeba-Timestamp':timestamp, 'Beeba-Sign': ''}
allure.environment(host="123.57.9.176", test_vars="比巴微商城测试环境")
@allure.feature('地址api测试')
class adddress_01(unittest.TestCase):
    def setUP(self):
        pass

    @allure.story('001验证用户添加新地址')
    def test_ad_address0101(self):
        '''添加正确信息地址并设置为默认地址'''
        url05 = url+'/api/v1/user-addresses'
        data_b = {'area_info': '广东省深圳市南山区',  # 省市区
                  'truename': '张涛',  # 联系人
                  'phone': '18688118811',  # 电话
                  'address': '科技生态园6栋9层',  # 详细地址
                  'is_default': '1',  # 是否默认 1 默认 0 不默认
                  'city_id': '19',
                  'area_id': '19'
                  }
        r = requests.post(url=url05,headers=headers_a,data=data_b)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_ad_address0102(self):
        '''添加地址验证联系人为空'''
        url05 = url+'/api/v1/user-addresses'
        data_b = {'area_info': '广东省深圳市南山区',  # 省市区
                  'truename': '',  # 联系人
                  'phone': '18688118811',  # 电话
                  'address': '科技生态园6栋9层',  # 详细地址
                  'is_default': '1',  # 是否默认 1 默认 0 不默认
                  'city_id': '19',
                  'area_id': '19'
                  }
        r = requests.post(url=url05,headers=headers_a,data=data_b)
        result=r.json()
        msg='联系人不能为空。'
        self.assertEqual(msg,result['errmsg'])

    def test_ad_address0103(self):
        '''添加地址验证联系人为空'''
        url05 = url+'/api/v1/user-addresses'
        data_b = {'area_info': '广东省深圳市南山区',  # 省市区
                  'truename': '测试',  # 联系人
                  'phone': '18688118811',  # 电话
                  'address': '',  # 详细地址
                  'is_default': '1',  # 是否默认 1 默认 0 不默认
                  'city_id': '19',
                  'area_id': '19'
                  }
        r = requests.post(url=url05,headers=headers_a,data=data_b)
        result=r.json()
        msg='详细地址不能为空。'
        self.assertEqual(msg,result['errmsg'])

    @allure.story('002验证修改用户单个地址')
    def test_amodify_address0101(self):
        '''002验证修改用户单个地址'''
        url06 = url+'/api/v1/user-addresses/25'
        data_b = {'area_info': '广东省深圳市南山区',  # 省市区
                  'truename': '比巴',  # 联系人
                  'phone': '18688118811',  # 电话
                  'address': '科技生态园6栋9层',  # 详细地址
                  'is_default': '1',  # 是否默认 1 默认 0 不默认
                  'city_id': '19',
                  'area_id': '19'
                  }
        r = requests.put(url=url06,headers=headers_a,data=data_b)
        result=r.json()
        msg='比巴'
        self.assertEqual(msg,result['data']['truename'])

    @allure.story('003验证删除用户单个地址')
    def test_n_delete_address0101(self):
        '''003验证删除用户单个地址'''
        url07 = url+'/api/v1/user-addresses/'+M
        r = requests.delete(url=url07,headers=headers_a)
        result=r.json()
        msg='删除成功'
        self.assertEqual(msg,result['errmsg'])

    @allure.story('004验证查看用户地址列表')
    def test_lall_address0101(self):
        '''004验证查看用户地址列表'''
        url08 = url+ '/api/v1/user-addresses'
        r = requests.get(url=url08,headers=headers_a)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    @allure.story('005验证查看用户单个地址')
    def test_lone_address0101(self):
        '''查看存在的地址'''
        url09 = url+'/api/v1/user-addresses/15'
        r = requests.get(url=url09,headers=headers_a)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_lone_address0102(self):
        '''查看不存在的地址'''
        url09 = url+'/api/v1/user-addresses/1'
        r = requests.get(url=url09,headers=headers_a)
        result=r.json()
        msg='资源不存在'
        self.assertEqual(msg,result['errmsg'])


    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()


