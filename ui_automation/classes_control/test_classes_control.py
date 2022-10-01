# -*- coding:utf-8 -*-
"""班次管理"""
from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.classes_control.classes_control import ClassdesControl
import pytest

class TestClasses_control():

    def setup_class(self):
        self.test = LargeModule()
        self.test1 = ClassdesControl(self.test.drvier)

    @pytest.mark.parametrize(('name'),[('测试')])
    def test_add_classify(self,name):
        self.test.classes_control().add_classify(name)


    @pytest.mark.parametrize(('name','edit_name'),[('测试','测试1')])
    def test_edit_classify(self,name,edit_name):
        self.test1.edit_classify(name,edit_name)

    @pytest.mark.parametrize(('name','headline','target','trainee'),[('测试1','test','测试目标','训练对象')])
    def test_add_classes(self,name,headline,target,trainee):
        self.test1.add_classes(name,headline,target,trainee)

    @pytest.mark.parametrize(('name','teacher'),[('课程名称','test006')])
    def test_add_classes_details(self,name,teacher):
        self.test1.add_classes_details(name, teacher)


    @pytest.mark.parametrize(('drill_name','nade_name'),[('训练名称','测试1')])
    def test_add_classes_details_drill(self,drill_name,nade_name):
        self.test1.add_classes_details_drill(drill_name,nade_name)

    @pytest.mark.parametrize(('section_name', 'teacher'), [('章节名称', 'test006')])
    def test_add_section(self,section_name,teacher):
        self.test1.add_section(section_name,teacher)

    @pytest.mark.parametrize(('name'),[('引用案例'),('引用知识点'),('引用法规')])
    def test_add_section_quote_laws(self,name):
        self.test1.add_section_quote_laws(name)


    @pytest.mark.parametrize(('name','add_name','file'),[('新建视频','vudeo_name','D:/dvieo/test_video.mp4'),('新建音频','audio_name','D:/dvieo/test_audio.mp3'),('OFFICE','office_name','D:/dvieo/test_office.xls'),('PDF','pdf_name','D:/dvieo/test_pdf.pdf'),('图片','picture_name','D:/dvieo/test_picture.jpeg')])
    def test_add_section_video(self,name,add_name,file):
        self.test1.add_section_video(name,add_name,file)


    @pytest.mark.parametrize(('task_headline','file','teacher'),[('task_headline','D:/dvieo/test_video.mp4','test006')])
    def test_add_scenario_task(self,task_headline,file,teacher):
        self.test1.add_scenario_task(task_headline,file,teacher)


    @pytest.mark.parametrize(('drill_headline','test'),[('drill_headline','这是测试训练')])
    def test_add_freedom_drill(self,drill_headline,test):
        self.test1.add_freedom_drill(drill_headline,test)

