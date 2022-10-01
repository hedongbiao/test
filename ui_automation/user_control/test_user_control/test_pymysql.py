# -*- coding:utf-8 -*-
from shangxue.ui_automation.user_control.mysql_sql import Pymysqll
import pytest


import yaml
class TestPymysql():

    def setup_class(self):
        self.test = Pymysqll()





    #@pytest.mark.parametrize('name',yaml.safe_load(open("../tada_yamy/user_data.yaml")))
    @pytest.mark.parametrize(('name'),[('test1'),('test2'),('test3'),('test4')])
    def test_del_mysql(self,name):
        self.test.db_del(name)




    # @pytest.mark.parametrize(('name'),[('test5')])
    # def test_select_mysql(self,name):
    #     self.test.db_select(name)