import traceback

import requests
#import requests,json
import pytest
from shangxue2.bash.test_xls import TestXls
import json
from shangxue2.bash.admin import Admin
# 导入被测的api模块
from shangxue2.bash.user_api import UserApi
import xlwt
import xlrd
from xlutils.copy import copy
import os.path
sheet1 = xlrd.open_workbook('D:/python/shangxue/bash/test.xls').sheet_by_name("Sheet2")
list = []
row1 = sheet1.row_values(0)
num = len(sheet1.col_values(0))
for index in range(3,num):
    list.append(sheet1.row_values(index,0,len(row1)))
print(list)

class TestBash():

    def setup_class(self):

        self.user_api = UserApi(org_code="TDS", username="admin", password="CD90EE3A79DF4251")
        resp = self.user_api.get_token()
        #print(json.dumps(resp.json()))
        self.refresh_token = resp.json().get("data").get("token")
        token = self.refresh_token
      
    @pytest.mark.parametrize("item",list)
    def test_post_req(self,item):
        contentType = None
        keyType = None

        if item[6] == 1:                    #json
            contentType = 'application/json'
            keyType = "json"

        if item[6] == 2:                    #table
            contentType = 'multipart/form-data'
            keyType = "data"

        if item[6] == 3:                    #form-urlencoded
            contentType = 'application/x-www-form-urlencoded'
            keyType = "data"

        if contentType == None or keyType == None:
            print("contentType 或者 keyType 为空")

        data = {
                "url":f"{item[2]}{item[3]}",
                "method": f"{item[4]}",
                "headers": {'x-auth-token': f"Bearer {self.refresh_token}","Content-Type":contentType},
                keyType:json.loads(item[5])
            }
        res = requests.request(**data)
        codeCol = item[7]
        code = res.json().get("code")
        print(data)
        if codeCol == 1 and codeCol == code:
            print("用例通过")
            asse = "用例通过"

        elif codeCol == 0 and codeCol == code:
            print("用例通过",res.json())
            asse = "用例通过",str(res.json())

        else:
            print(res.json())
            asse = str(res.json())

        rb = xlrd.open_workbook('D:/python/shangxue/bash/test.xls',formatting_info=True)
        r_sheet = rb.sheet_by_index(0)
        wb = copy(rb)
        sheet = wb.get_sheet(1)
        itemCol1 = str.split(item[0],"_")
        try:
            index = int(itemCol1[1]) #这行报错是由于Excel表格id列未配置导致的
            index = index + 2
            sheet.write(index,9,asse)
            wb.save("D:/python/shangxue/bash/test.xls")
            print(res.json())
        except Exception as e:
            log = ""
            if len(itemCol1)!=2:
                log = "1、当前id 配置不正确\n"
            print("Excel 写入失败，请检查当前用例配置问题 可能的原因有：\n"+log)
            traceback.print_exc()


                # pass #不通过写入excel
        # else:
        #     clsData = str.split(item[8],"~")
        #     if len(clsData) == 2:
        #         key = clsData[0]
        #         value = clsData[1]
        #         if item[7]  == res.json().get("code") and value == res.json().get("data").get(key):
        #             print("用例通过")
        #         else:
        #             print(res.json())
        #     else:
        #         value = clsData[0]
        #         if item[7]  == res.json().get("code") and value == res.json().get("data"):
        #             print("用例通过")
        #         else:
        #             print(res.json())

        # print(data)
        # print(res.json())


    # def test_post_req(self):
        # resps = self.user_api.user_list1(self.refresh_token)
        #
        # for index in resps:
        #     print(index,resps[index].json())
        # resp = self.user_api.user_list1(self.refresh_token)
        #print("="*1)
        # print(resp.json())
    # def test_a(self):
    #     assert True

