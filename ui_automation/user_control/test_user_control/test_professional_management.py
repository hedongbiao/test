# -*- coding:utf-8 -*-
import pytest
from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.user_control.user_moduel import UserModuel

class TestProfessionalManagement():

    def setup_class(self):
        self.test = LargeModule()
        self.test1 = UserModuel(self.test.drvier)


    @pytest.mark.parametrize(('serial_number','headline'),[('123','测试'),('234','测试2')])
    def test_add_professional_management(self,serial_number,headline):
        self.test.user_control().professional_management().add_professional_management(serial_number,headline)

    @pytest.mark.parametrize(('headline'),[('测试1')])
    def test_edit_professional_management(self,headline):
        self.test1.professional_management().edit_classify(headline)

    @pytest.mark.parametrize(('name'),[('测试1')])
    def test_delete_professional_management(self,name):
        self.test1.professional_management().delete_professional_management(name)

