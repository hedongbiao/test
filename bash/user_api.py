"""
这类放所有跟user，
"""
import pytest
import xlrd
# 这里继承公共业务，方便获取token的方法。
from shangxue2.bash.admin import Admin
import json
from shangxue2.bash.test_xls import TestXls
sheet1 = xlrd.open_workbook(r'D:/python/shangxue/bash/test.xls').sheet_by_name("Sheet1")
list = []
row1 = sheet1.row_values(0)
num = len(sheet1.col_values(0))
for index in range(2,num):
    list.append(sheet1.row_values(index,0,len(row1)))

class UserApi(Admin):

    def user_list(self, token):
        data = {
            "url": "",
            "method": "post",
            "headers": {'Content-Type':'application/json','x-auth-token': f"Bearer {token}"},
            "json": {
                "page": 1,
                "limit": 10,
                "sort": "",
                "order": "",
                "params": {
                    "status":"OK",
                    "weChat": "", # 微信(传 WECHAT 参数代表是获取微信用户)
                    "relatedInd":"",  #  条件（0：未关联用户、1:关联用户。不传则直接都获取所有微信用户）
                    "deptIds": "",
                    "q": ""
                          }
                    }
                }

        return self.do_request(data)

    # @pytest.mark.parametrize("item","token",list,token)
    # def user_list1(self,item,token):
        # test = list[0]
        # resps = {}
        # for item in list:
        #    # print(list)
        #     print(list)
        #     data = {
        #         "url":f"{item[2]}{item[3]}",
        #         "method": f"{item[4]}",
        #         "headers": {'Content-Type':'application/json','x-auth-token': f"Bearer {token}"},
        #         "json":json.loads(item[5])
        #
        #     }
        #     resps[item[0]]=self.do_request(data)
        # return resps
