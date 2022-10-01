# -*- coding:utf-8 -*-
from time import sleep

import pytest

from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.resource_library.knowle import Knowle




class TestResoueceLibrary():

    def setup_class(self):
        self.test = LargeModule()
        self.test1 = Knowle(self.test.drvier)
        self.test2 = '测试1'


    def test_knowledge_add_classify(self):
        #知识点分类新增

        self.test.rwsource().knowle().add_classify()
        sleep(1)


    def test_knowledge_edit_classify(self):
        #知识点分类编辑
        self.test1.knowle().edit_classify()


    def test_knowledge_add_video(self):
        #知识点新增视频
        self.test1.classify().add_video()


    def test_knowledge_add_office(self):
        #知识点新增office
        self.test1.classify().add_office()


    def test_knowledge_add_pdf(self):
        #知识点新增pdf
        self.test1.classify().add_pdf()


    def test_knowledge_add_audio(self):
        #知识点新增音频
        self.test1.classify().add_audio()


    def test_knowledge_add_picture(self):
        #知识点新增图片
        self.test1.classify().add_picture()


    def test_knowledge_edit(self):
        #编辑知识点内容
        self.test1.classify().edit_details()


    def test_knowledge_operate(self):
        #知识点内容操作
        self.test1.classify().operate_details()


    def test_knowledge_file_operate(self):
        #已归档知识点操作
        self.test1.classify().file_operate_details()

    def test_knowledge_dilite(self):
        #删除知识点内容及分类
        self.test1.classify().dilite_details_classify()

