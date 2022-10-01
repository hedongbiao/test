# -*- coding:utf-8 -*-
"""知识比武"""
from time import sleep

from selenium.webdriver.common.by import By

from shangxue.ui_automation.base_page import BasePage

class KnowledgeContest(BasePage):

    def edit(self,name):
        #分类编辑
        sleep(1)
        self.find(By.XPATH,'//input[@maxlength="8"]').clear()
        self.find(By.XPATH, '//input[@maxlength="8"]').send_keys(name)
        self.finds(By.XPATH,'//div[@id="pane-first"]/div[2]/button/span')[0].click()
        sleep(1)
        self.finds(By.XPATH,'//div[@id="pane-second"]/div[1]//img')[0].click()
        sleep(1)
        self.find(By.XPATH,'//div[contains(text(),"admin")]').click()
        self.find(By.XPATH,'//div[@aria-label="请选择"]/div[3]/span/button[2]').click()
        sleep(1)
        self.find(By.XPATH, '//span[contains(text(),"保存")]').click()
        sleep(1)
        self.finds(By.XPATH,'//span[contains(text(),"返回")]')[2].click()
        return ()


    def add_answer(self,headline,pattern):
        #新增主题
        sleep(1)
        self.find(By.XPATH, '//span[contains(text(),"新增")]').click()
        self.find(By.XPATH,'//input[@maxlength="20"]').send_keys(headline)
        self.finds(By.XPATH,'//input[@placeholder="请选择"]')[0].click()
        self.find(By.XPATH,f'//span[text() = "{pattern}"]')
        self.find(By.XPATH,'//span[contains(text(),"保存")]').click()
        return ()

    def add_question_bank(self,content,answer1,answer2):
        #新增题目
        sleep(1)
        self.find(By.XPATH, '//span[contains(text(),"题库")]').click()
        self.find(By.XPATH, '//span[contains(text(),"新增")]').click()
        self.find(By.CSS_SELECTOR,'.ql-editor.ql-blank').send_keys(content)
        self.finds(By.XPATH,'//input[@maxlength="200"]')[0].send_keys(answer1)
        self.finds(By.XPATH,'//input[@maxlength="200"]')[1].send_keys(answer2)
        self.find(By.XPATH, '//span[contains(text(),"保存")]').click()
        return ()

    def edit_question_bank(self,answer):
        sleep(1)
        self.find(By.XPATH,'//i[@class="el-icon-edit"]').click()
        self.finds(By.XPATH, '//input[@maxlength="200"]')[2].send_keys(answer)
        self.find(By.XPATH, '//span[contains(text(),"保存")]').click()
        return ()

    

