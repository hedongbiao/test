# -*- coding:utf-8 -*-
import pytest

from shangxue.ui_automation.large_module import LargeModule
from shangxue.ui_automation.knowledge_contest.knowledge_contest import KnowledgeContest


class TestKnowledgeContest():

    def setup_class(self):
        self.test = LargeModule()
        self.test1 = KnowledgeContest(self.test.drvier)

    @pytest.mark.parametrize(('name'),[('人机对战1')])
    def test_man_fighting_edit(self,name):
        self.test.knowledge_Contest().man_machine_fighting().edit(name)

    @pytest.mark.parametrize(('name'),[('练习模式')])
    def test_Practice_mode_edit(self,name):
        self.test.knowledge_Contest().Practice_mode().edit(name)

    @pytest.mark.parametrize(('name'), [('普通练习1')])
    def test_practice_common_edit(self,name):
        self.test.knowledge_Contest().practice_common_edit().edit(name)

    @pytest.mark.parametrize(('name'), [('错题练习1')])
    def test_practice_Wrong_title_edit(self,name):
        self.test.knowledge_Contest().practice_Wrong_title_edit().edit(name)

    @pytest.mark.parametrize(('name'),[('排位赛1')])
    def test_qualifying_tournament_edit(self,name):
        self.test.knowledge_Contest().qualifying_tournament_edit().edit(name)

    @pytest.mark.parametrize(('headline','pattern'),[('主题1','人机对战')])
    def test_add_theme(self,headline,pattern):
        self.test.knowledge_Contest().man_machine_fighting().add_answer(headline,pattern)

    @pytest.mark.parametrize(('content','answer1','answer2'),[('test1','1','2'),('test2','1','2'),('test3','1','2')])
    def test_add_question_bank(self,content,answer1,answer2):
        self.test1.add_question_bank(content,answer1,answer2)




