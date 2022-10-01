# -*- coding:utf-8 -*-
"""知识比武"""
from time import sleep

from selenium.webdriver.common.by import By

from shangxue.ui_automation.base_page import BasePage
from shangxue.ui_automation.knowledge_contest.knowledge_contest import KnowledgeContest

class ThemeList(BasePage):

    def practice_pattern(self):
        #判断练习模式是否展开
        listbtn = self.find(By.XPATH,"//div[contains(text(),'练习模式')]")
        style = self.find(By.CSS_SELECTOR,'.list-item.showNull')
        if not style is None:
            listbtn.click()
            return BasePage
        else:

            return BasePage

    def title_set(self):
        listbtn = self.find(By.XPATH,"//div[contains(text(),'头衔设置')]")
        style = self.find(By.CSS_SELECTOR,'.el-collapse-item__header.is-active')
        if not style:
            listbtn.click()
            return BasePage
        else:
            return BasePage

    def man_machine_fighting_edit(self):
        #人机模块编辑
        self.finds(By.XPATH, '//i[@class="el-icon-edit"]')[0].click()
        return KnowledgeContest(self.drvier)

    def Practice_mode(self):
        #练习模式编辑
        self.finds(By.XPATH, '//i[@class="el-icon-edit"]')[1].click()
        return KnowledgeContest(self.drvier)

    def practice_common_edit(self):
        # 普通练习编辑
        self.practice_common()
        sleep(1)
        self.finds(By.XPATH, '//i[@class="el-icon-edit"]')[1].click()
        return KnowledgeContest(self.drvier)

    def practice_Wrong_title_edit(self):
        # 错题练习编辑
        self.practice_Wrong_title()
        self.finds(By.XPATH, '//i[@class="el-icon-edit"]')[1].click()
        return KnowledgeContest(self.drvier)

    def qualifying_tournament_edit(self):
        #排位赛编辑
        self.qualifying_tournament()
        sleep(1)
        self.finds(By.XPATH,'//i[@class="el-icon-edit"]')[1].click()
        return KnowledgeContest(self.drvier)

    def man_machine_fighting(self):
        #人机对战点击
        self.find(By.XPATH, "//div[contains(text(),'人机对战')]").click()
        return KnowledgeContest(self.drvier)


    def practice_common(self):
        #普通练习点击
        self.practice_pattern()
        sleep(1)
        self.find(By.XPATH,"//div[contains(text(),'普通练习')]").click()
        return KnowledgeContest(self.drvier)

    def practice_Wrong_title(self):
        #错题练习点击
        self.practice_pattern()
        self.find(By.XPATH, "//div[contains(text(),'错题练习')]").click()
        return KnowledgeContest(self.drvier)

    def qualifying_tournament(self):
        #排位赛点击
        self.find(By.XPATH, "//div[contains(text(),'排位赛')]").click()
        return KnowledgeContest(self.drvier)

    def title_manage(self):
        #头衔管理点击
        self.title_set()
        self.find(By.XPATH, "//div[contains(text(),'头衔管理')]").click()
        return KnowledgeContest(self.drvier)