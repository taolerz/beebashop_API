# -*- coding:utf8 -*-
import pymysql
from sshtunnel import SSHTunnelForwarder
class mysql00():
    def mysql008(self):
        # MySQL数据库ssh连接脚本
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
            # port=server.local_bind_port)
            port=server.local_bind_port)
        cursor = myConfig.cursor()
        # myConfig.commit()
        # 关闭数据库连接
        # cursor.close()
        cursor.execute('SELECT id FROM bb_user_address ORDER BY id desc LIMIT 1')
        D = cursor.fetchone()
        print(D)
        M = str(D[0])
        return M





