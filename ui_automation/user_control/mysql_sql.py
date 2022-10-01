# -*- coding:utf-8 -*-

import pymysql
import time



class Pymysqll():

    def __init__(self):
        self.conn = pymysql.connect(
            host='8.134.59.220',
            port=15071,
            user='root',
            password='aabb@ccdd',
            database='tds_microservices',
            charset='utf8')

        self.title = time.strftime('%H:%M:%S',time.localtime(time.time()))
#删


        # 查
    def db_select(self, name):
        cursor = self.conn.cursor()
        sql = f"SELECT * FROM sys_user where username='{name , self.title}'"
        cursor.execute(sql)
        self.datalist = []
        res = cursor.fetchall()
        for s in res:
            self.datalist.append(s[0])

        print(self.datalist)

    def db_del(self,name):
        try:
            cursor = self.conn.cursor()
            sql = f"DELETE FROM sys_actor_relation WHERE child_id IN (SELECT id FROM sys_user WHERE username='{name+self.title}') AND type='USR_CURRENT_DPT';"
            sql1 = f"delete from sys_user where username='{name}'"
            cursor.execute(sql)
            cursor.execute(sql1)
            print(sql)
            self.conn.commit()
            cursor.close()
        except:
            print("删除失败")
        else:
            print("删除成功")
        return ()


# #增
# def db_add(name,pwd):
#     try:
#         cursor = conn.cursor()
#         sql = "insert into user(user_name,user_pwd) VALUES('%s','%s')" % (name, pwd)
#         cursor.execute(sql)
#         conn.commit()
#         cursor.close()
#     except:
#         print("添加失败")
#     else:
#         print("添加成功")


# #改
# def db_update(name,new_name):
#     try:
#         cursor = conn.cursor()
#         sql = "update user set user_name='%s' where user='%s' " % (new_name, name)
#         cursor.execute(sql)
#         conn.commit()
#         cursor.close()
#     except:
#         print("更改失败")
#     else:
#         print("更改成功")
#



