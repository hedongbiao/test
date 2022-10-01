# -*- coding:utf-8 -*-
import pytest

from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.resource_library.knowle import Knowle


class TestCertificateTemplate():

    def setup_class(self):
        self.test1 = LargeModule()
        self.test2 = Knowle(self.test1.drvier)


    def test_itembank_add_classify(self):
        # 新增证书模板分类
        self.test1.rwsource().certificate_template().add_classify()


    def test_itrmbank_edit_classify(self):
        # 编辑证书模板分类
        self.test2.certificate_template().certificate_edit_classify()

    @pytest.mark.parametrize(('name'), [('测试1'), ('测试2'), ('测试3'), ('测试4')])
    def test_add_certificate_template(self,name):
        #新增证书模板
        self.test2.classify().add_certificate_template(name)


    def test_edit_certificate_template(self):
        #证书模板编辑
        self.test2.classify().certificate_template_edit_details()


    def test_certificate_template_delete(self):
        #删除证书模板及分类
        self.test2.classify().certificate_template_delete()