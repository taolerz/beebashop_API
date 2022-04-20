import time,unittest,requests
import json,allure
from beebashop_API.common.common import url,Authorization,timestamp

@allure.feature('团队')
class beeba_team(unittest.TestCase):
    def setUp(self):
        pass

    def test_myinvitation(self):
        '''我的邀请'''
        url_016 = url+'/api/v1/user-inviters'
        headers06 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_016,headers=headers06)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_useragents(self):
        '''我的团队'''
        url_017 = url+'/api/v1/user-agents'
        headers17 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_017,headers=headers17)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_useragentschildren(self):
        '''我的团队下级；会报缺少参数：id，因为还没有下级'''
        url_018 = url+'/api/v1/user-agents/children'
        headers18 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_018,headers=headers18)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_useragents01(self):
        '''我的团队详情'''
        url_019 = url+'/api/v1/user-agents/1'
        headers19 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_019,headers=headers19)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_useragents02(self):
        '''注册审核'''
        url_020 = url+'/api/v1/user-agents/1'
        headers20 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.get(url=url_020,headers=headers20)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_useragents03(self):
        '''审核。提示页面未找到，需要有审核单'''
        url_021 = url+'/api/v1/user-agent-applies'
        headers21 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        r=requests.post(url=url_021,headers=headers21)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def test_useragents04(self):
        '''注册审核修改（通过、驳回）。报错是因为需要有审核单'''
        url_022 = url+'/api/v1/user-agent-applies/change'
        headers22 = {'Authorization': Authorization,
                     'Beeba-Timestamp': timestamp,
                     'Beeba-Sign': ''}
        data22 = {'status':'0',
                  'user_id':'3'}
        r=requests.post(url=url_022,headers=headers22)
        result=r.json()
        msg='ok'
        self.assertEqual(msg,result['errmsg'])

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()
