# -*- coding:utf-8 -*-
import pytest
from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.user_control.user_moduel import UserModuel

class TestPostManagement():

    def setup_class(self):
        self.test = LargeModule()
        self.test1 = UserModuel(self.test.drvier)

    @pytest.mark.parametrize(('serial_number', 'headline'), [('123', '测试'), ('234', '测试2')])
    def test_add_post(self,serial_number,headline):
        self.test.user_control().post_management().add_post(serial_number,headline)

    @pytest.mark.parametrize(('headline'), [( '测试1')])
    def test_edit_post(self,headline):
        self.test1.post_management().edit_classify(headline)

    @pytest.mark.parametrize(('name'), [('测试1')])
    def test_delete_post(self,name):
        self.test1.post_management().delete_post(name)