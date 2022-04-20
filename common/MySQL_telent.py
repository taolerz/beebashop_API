# -*- coding:utf8 -*-
import pymysql
from sshtunnel import SSHTunnelForwarder
from beebashop_API.common.common import url

#MySQL数据库ssh连接脚本
server = SSHTunnelForwarder(
    ssh_address_or_host=('123.57.9.176', 22),  # 指定ssh登录的跳转机的address
    ssh_username='root',  # 跳转机的用户
    ssh_password='beeba^pG(x|Y)o!Y07q',  # 跳转机的密码
    remote_bind_address=('127.0.0.1', 3306))
server.start()
myConfig = pymysql.connect(
    user="root",
    passwd="Bb168460",
    host="127.0.0.1",
    db='store',
    #port=server.local_bind_port)
    port=server.local_bind_port)
cursor =myConfig.cursor()
#myConfig.commit()
# 关闭数据库连接
#cursor.close()

cursor.execute('SELECT id FROM bb_user_address WHERE user_id="6" ORDER BY id desc LIMIT 1')
D = cursor.fetchone()
#print(D)
M = str(D[0])

cursor.execute('SELECT id FROM bb_cart ORDER BY id desc LIMIT 1')
BB = cursor.fetchone()
NN = str(BB[0])

cursor.execute('SELECT id FROM bb_cash WHERE state="1" AND user_id="6" ORDER BY id DESC LIMIT 1')
XXB = cursor.fetchone()
TX = str(XXB[0])

cursor.execute('SELECT order_id FROM bb_order_goods WHERE to_id="6" ORDER BY id DESC LIMIT 1')
dd = cursor.fetchone()
DDXQ = str(dd[0])   #单个订单详情

cursor.execute('SELECT id FROM bb_order WHERE to_id="6" AND status="10" ORDER BY id DESC LIMIT 1')
qx = cursor.fetchone()
QXDD = str(qx[0])   #取消未支付的订单

cursor.execute('SELECT id FROM bb_order WHERE to_id="6" AND status="30" ORDER BY id DESC LIMIT 1')
wc = cursor.fetchone()
WCDD = str(wc[0])     #完成订单

cursor.execute('SELECT id FROM bb_order WHERE to_id="6" AND status="30" ORDER BY id DESC LIMIT 1')
xj = cursor.fetchone()
XJDD = str(xj[0])     #我的下级待付款订单号

cursor.execute('SELECT id FROM bb_order WHERE to_id="6" AND status="30" ORDER BY id DESC LIMIT 1')
yifu1 = cursor.fetchone()
XJYF1 = str(yifu1[0])     #我的下级已付款订单号

#print(M)
# 另外一种方法
# def get_unpublished_data():
#     server_id = '123.57.9.176'
#     ssh_password = 'beeba^pG(x|Y)o!Y07q'
#     ssh_username = 'root'
#
#     with SSHTunnelForwarder((server_id, 22),
#         ssh_password=ssh_password,
#         ssh_username=ssh_username,
#         remote_bind_address= ('127.0.0.1', 3306)) as server:
#         db = pymysql.connect(host='127.0.0.1',
#                         port = server.local_bind_port,
#                         user = 'root',
#                         passwd = 'Bb168460',
#                         db = 'store',
#                         charset = 'utf8') #这里的地址也是本地的localhost
#
#     cursor = db.cursor()
#     sql = 'SELECT id FROM bb_user_address ORDER BY id desc LIMIT 1'
#     effect = cursor.execute(sql)
#     db_result = cursor.fetchall()
#     db.commit()
