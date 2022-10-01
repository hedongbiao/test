# -*- coding:utf-8 -*-

import pytest

from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.resource_library.knowle import Knowle

class TestPaerWarehouse():

    def setup_class(self):
        self.test1 = LargeModule()
        self.test2 = Knowle(self.test1.drvier)

    def test_paer_warehouse_add_classify(self):
        #新增试卷库分类
        self.test1.rwsource().test_paper_warehouse().add_classify()

    def test_paer_wareshouse_edit_classify(self):
        # 编辑试卷库分类
        self.test2.test_paper_warehouse().itembank_edit_classify()

    @pytest.mark.parametrize(('headline'), [('测试1'),('测试2'), ('测试3'), ('测试4'),('测试5')])
    def test_add_testpaer(self,headline):
        #新增试卷
        self.test2.classify().test_add_testpaer(headline)


    def test_edit_testpaer(self):
        #操作试卷内容
        self.test2.classify().testpaper_edit_details()

    def test_testpaer_file_operate_details(self):
        self.test2.classify().testpaer_file_operate_details()
