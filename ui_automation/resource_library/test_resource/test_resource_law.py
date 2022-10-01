# -*- coding:utf-8 -*-

from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.resource_library.knowle import Knowle


class TestLaw():

    def setup_class(self):
        self.test1 = LargeModule()
        self.test2 = Knowle(self.test1.drvier)

    def test_law_add_classify(self):
        #新增法律法规
        self.test1.rwsource().law().add_classify()


    def test_law_edit_classify(self):
        #编辑法律法规分类
        self.test2.law().edit_classify()

    def test_law_add_video(self):
        # 法律法规新增视频
        self.test2.classify().add_video()

    def test_law_add_office(self):
        # 法律法规新增office
        self.test2.classify().add_office()

    def test_law_add_pdf(self):
        # 法律法规新增pdf
        self.test2.classify().add_pdf()

    def test_law_add_audio(self):
        # 法律法规新增音频
        self.test2.classify().add_audio()

    def test_law_add_picture(self):
        # 法律法规新增图片
        self.test2.classify().add_picture()

    def test_law_edit(self):
        # 编辑法律法规内容
        self.test2.classify().edit_details()

    def test_law_operate(self):
        # 法律法规内容操作
        self.test2.classify().operate_details()

    def test_law_file_operate(self):
        # 已归档法律法规操作
        self.test2.classify().law_file_operate_details()

    def test_law_dilite(self):
        # 删除法律法规内容及分类
        self.test2.classify().dilite_details_classify()

