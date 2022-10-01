# -*- coding:utf-8 -*-

import pytest
from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.resource_library.knowle import Knowle
import allure

@allure.feature("知识点标签")
class TestKnowledgeLabel():

    def setup_class(self):
        self.test1 = LargeModule()
        self.test2 = Knowle(self.test1.drvier)

    @allure.story("新增知识点分类")
    def test_knowledge_label_add_classify(self):

        self.test1.rwsource().knowledge_label().add_classify()

    @allure.story("编辑知识点分类")
    def test_knowledge_label_edit_classify(self):

        self.test2.knowledge_label().edit_classify()

    @allure.story("新增知识点标签")
    @pytest.mark.parametrize(('name'), [('测试1'), ('测试2'), ('测试3'), ('测试4')])
    def test_add_knowledge_label(self,name):

        self.test2.classify().add_knowledge_label(name)

    @allure.story("操作知识点标签")
    def test_operate_knowledge_label(self):
        self.test2.classify().operate_knowledge_label()