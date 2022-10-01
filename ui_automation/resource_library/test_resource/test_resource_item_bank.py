# -*- coding:utf-8 -*-
import pytest

from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.resource_library.knowle import Knowle

class TestItemBank():

    def setup_class(self):
        self.test1 = LargeModule()
        self.test2 = Knowle(self.test1.drvier)
        self.headline = '编辑试题库分类'

    def test_itembank_add_classify(self):
        #新增试题库分类
        self.test1.rwsource().itrmbank().add_classify()



    def test_itrmbank_edit_classify(self):
        #编辑试题库分类
        self.test2.itrmbank().itembank_edit_classify()

    @pytest.mark.parametrize(('test'), [('测试1'), ('测试2'), ('测试3'), ('测试4'),('测试5'),('测试6'),('测试7'),('测试8')])
    def test_itembank_add_topic(self,test):
        #新增试题
        self.test2.classify().add_topic(test)

    # def test_import_data(self):
    #     #导入试题
    #     self.test2.classify().import_data()


    def test_itembank_edit_details(self):
        #试题功能操作
        self.test2.classify().itembank_edit_details()


    def test_itembank_pigeonhole(self):
        #批量归档
        self.test2.classify().pigeonhole()


    def test_itembank_file_operate_details(self):
        #已归档操作
        self.test2.classify().itembank_file_operate_details()


    def test_delete_topic(self):
        self.test2.classify().empty_topic()




