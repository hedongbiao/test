

import json
import xlrd
import pytest

sheet1 = xlrd.open_workbook(r'D:/python/shangxue/bash/test.xls').sheet_by_name("Sheet1")
list = []
row1 = sheet1.row_values(0)
num = len(sheet1.col_values(0))
for index in range(2,num):
    list.append(sheet1.row_values(index,0,len(row1)))

class TestXls:
    def test_xls(self):


        wordbook= xlrd.open_workbook(r'D:/python/shangxue/bash/test.xls')
        sheet1 = wordbook.sheet_by_name("Sheet1")#获取sheet
        sheet2 = wordbook.sheet_by_name('Sheet2')
        # rows = sheet2.row_values(0) # 获取第四行内容
        # cols = sheet2.col_values(2) # 获取第三列内容
        # self.print_item(sheet2)
        # print(rows)
        # table = self.get_xls_data_by_table(sheet1)

        list = self.get_xls_data_by_list(sheet1)
        # print(table)
        uri = "uri"
        url = "url"
        Id = "index_" + str(1)
        # print(table[Id][uri]+table[Id][url])
        # for item in table: #字典
        #     print("id:"+item+"   url:"+table[item][uri]+table[item][url])

        for item in list:   #列表
            # print("id:" + item["id"] +"url:"+item[uri]+item[url])
            self.uri = item["uri"]
            self.url = item["url"]
            self.request = item["request"]
            self.params = item["params"]
            #print(self.uri)
            #print(list)

    def get_xls_data_by_list(self,sheet):
        row1 = sheet.row_values(0)
        list = []
        num = len(sheet.col_values(0))
        # print("num的值：",num)
        for index in range(2,num):
            # print("index：",index)
            row_now = sheet.row_values(index,0,len(row1))
            data = {}
            # print("row1：",len(row1))
            for j in range(0,len(row1)):
                # print("data：",row1[j],row_now[j])
                data[row1[j]] = row_now[j]
            list.append(data)
        return list

    @pytest.mark.parametrize("test",list)
    def test_1(self,test):
        print(test[0],test[1],test[2],test[3],test[4],test[5],test[6],test[7])


    # def get_xls_data_by_table(self,sheet):
    #     row1 = sheet.row_values(0)
    #     table = {}
    #     num = len(sheet.col_values(0))
    #     # print("num的值：",num)
    #     for index in range(2,num):
    #         # print("index：",index)
    #         row_now = sheet.row_values(index,0,len(row1))
    #         data = {}
    #         # print("row1：",len(row1))
    #         for j in range(0,len(row1)):
    #             # print("data：",row1[j],row_now[j])
    #             data[row1[j]] = row_now[j]
    #         table[row_now[0]] = data
    #     return table

    # def print_item(self,sheet2):
    #     for index in range(0):
    #         for i in sheet2.row_values(index):
    #             print(i)



