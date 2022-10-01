# -*- coding:utf-8 -*-
import pytest

from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.resource_library.knowle import Knowle


class TestCase():

    def setup_class(self):
        self.test1 = LargeModule()
        self.test2 = Knowle(self.test1.drvier)


    def test_case_add_classify(self):
        # 新增案例
        self.test1.rwsource().case().add_classify()


    def test_case_edit_classify(self):
        # 编辑案例分类
        self.test2.case().edit_classify()


    def test_case_add_video(self):
        # 案例新增视频
        self.test2.classify().add_video()


    def test_case_add_office(self):
        # 案例新增office
        self.test2.classify().add_office()


    def test_case_add_pdf(self):
        # 案例新增pdf
        self.test2.classify().add_pdf()


    def test_case_add_audio(self):
        # 案例新增音频
        self.test2.classify().add_audio()


    def test_case_add_picture(self):
        # 案例新增图片
        self.test2.classify().add_picture()


    def test_case_edit(self):
        # 编辑案例内容
        self.test2.classify().edit_details()

    def test_case_operate(self):
        # 案例内容操作
        self.test2.classify().operate_details()

    def test_case_file_operate(self):
        # 已归档案例操作
        self.test2.classify().law_file_operate_details()


    def test_case_dilite(self):
        # 删除案例内容及分类
        self.test2.classify().dilite_details_classify()

