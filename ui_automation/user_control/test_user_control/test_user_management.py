# -*- coding:utf-8 -*-


import pytest
from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.user_control.user_moduel import UserModuel


class TestUserManagement():

    def setup_class(self):
        self.test = LargeModule()
        self.test1 = UserModuel(self.test.drvier)


    @pytest.mark.parametrize(('name','account','role'),[('测试2','test1','系统管理员'),('测试2','test2','培训管理员'),('测试2','test3','教员'),('测试2','test4','学员')])
    def test_add_user(self,name,account,role):
        self.test.user_control().user_management().add_user(name,account,role)


    @pytest.mark.parametrize(('name','password','account'),[('测试2','w123456','测试')])
    def test_edit_user(self,name,password,account):
        self.test1.user_management().edit_user(name,password,account)

    @pytest.mark.parametrize(('name'),[('测试2')])
    def test_del_user(self,name):
        self.test1.user_management().del_user(name)



