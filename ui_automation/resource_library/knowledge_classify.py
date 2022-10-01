# -*- coding:utf-8 -*-
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from shangxue.ui_automation.base_page import BasePage
import os
"""资源库"""

class KnowledgeClassify(BasePage):



    def add_classify(self):

        #分类新增
        sleep(2)
        self.drvier.find_element(By.XPATH,"//span[contains(text(),'新增')]").click()
        self.drvier.find_element(By.XPATH,"//input[@maxlength='30']").send_keys("测试")
        self.drvier.find_element(By.XPATH,"//span[contains(text(),'提交')]").click()
        return ('测试')


    def edit_classify(self):
        # 分类编辑
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试')]").click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'编辑')]").click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='30']").clear()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='30']").send_keys("测试1")
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'提交')]").click()
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'管理员权限')]").click()
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'指定管理员')]").click()
        # self.drvier.find_elements(By.XPATH, "//img[@class='pointAtGroup-icon']")[0].click()
        # self.drvier.find_element(By.XPATH, "//div[contains(text(),'admin')]").click()
        # self.drvier.find_element(By.XPATH,
        #                     "//*[@id='pane-second']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'教员权限')]").click()
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'指定教员')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//*[@id='pane-third']/div[1]/div/div[2]/div/div[2]/div[1]/img").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'test006')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH,
                            "//*[@id='pane-third']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
        self.drvier.find_element(By.XPATH, "//*[@id='pane-third']/div[2]/button[1]/span").click()
        return ('测试1')

    def add_video(self):
        # 新增视频
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'视频')]").click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("add_video")
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys(
            "C:/Users/Administrator/Videos/Captures/f3bbbf14b545e9366dc9e39daef0c2f8.mp4")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        return ('test_vudeo')

    def add_office(self):
        # 新增office
        self.drvier.find_elements(By.XPATH, "//button[@type='button']")[3].click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("add_office")
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_office.xls")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        return ('test_office')

    def add_pdf(self):
        # 新增pdf
        self.drvier.find_elements(By.XPATH, "//button[@type='button']")[4].click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("add_pdf")
        sleep(1)
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_pdf.pdf")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        return ('test_pdf')

    def add_audio(self):
        # 添加音频
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//button[@type='button']")[5].click()
        sleep(2)
        self.drvier.find_elements(By.XPATH, "//i[@class='el-icon-plus']")[6].click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("add_avdio")
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_audio.mp3")
        sleep(3)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        return ('test_audio')

    def add_picture(self):
        # 添加视频
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//button[@type='button']")[5].click()
        sleep(2)
        self.drvier.find_elements(By.XPATH, "//i[@class='el-icon-plus']")[7].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("add_picture")
        sleep(1)
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_picture.jpeg")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        return ('test_picture')

    def edit_details(self):
        # 编辑内容
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='编辑']")[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("te_ceshi")
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        return ('test_picture+1')

    def operate_details(self):
        # 内容操作
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='查看']")[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//button[@aria-label='Close']")[5].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='复制']")[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='归档']")[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='删除']")[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[3]/span/button[2]/span").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//i[@class="iconfont"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        return ('')

    def file_operate_details(self):
        # 已归档内容操作
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[@id='tab-second']").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='查看']")[5].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//button[@aria-label='Close']")[5].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='删除']")[5].click()
        sleep(2)
        self.drvier.find_elements(By.XPATH,
                                 '/html/body/div[@class="el-dialog__wrapper"]/div/div[3]/span/button[2]/span')[1].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='激活']")[0].click()
        sleep(1)

        # self.drvier.find_element(By.CSS_SELECTOR, '#pane-second .el-table__body tr:nth-child(1) label>span').click()
        self.drvier.find_element(By.XPATH,
                                 '//*[@id="pane-second"]//*[@class="el-table__body"]//tr[1]//label/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'激活')]").click()
        sleep(1)
        return ()

    def dilite_details_classify(self):
        # 删除内容及删除分类
        sleep(1)
        self.drvier.find_element(By.XPATH,
                                 '//*[@id="pane-second"]//table[@class="el-table__header"]//tr[1]//label/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//*[@id="pane-second"]//span[contains(text(),"删除")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//*[@id='admin']/div[2]/div/div[6]/div/div[3]/span/button[2]/span").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[@id='tab-first']").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"测试1")]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'删除')]")[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//*[@id="admin"]/div[2]/div/div[6]/div/div[3]/span/button[2]/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"测试1")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[@class="txt"][contains(text(),"删除")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/span/button[2]/span').click()
        return ('测试1')

    def law_file_operate_details(self):
        #法律法规已归档内容操作
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[@id='tab-second']").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='查看']")[5].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//button[@aria-label='Close']")[5].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='删除']")[5].click()
        sleep(2)
        self.drvier.find_elements(By.XPATH,
                                 '/html/body/div[@class="el-dialog__wrapper"]/div/div[3]/span/button[2]/span')[1].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='激活']")[0].click()
        sleep(1)

        # self.drvier.find_element(By.CSS_SELECTOR, '#pane-second .el-table__body tr:nth-child(1) label>span').click()
        self.drvier.find_element(By.XPATH,
                                 '//*[@id="pane-second"]//*[@class="el-table__body"]//tr[1]//label/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'激活')]").click()
        sleep(1)
        return ()

    def itembank_edit_classify(self):
        # 试题库分类编辑
        sleep(2)
        self.drvier.find_element(By.XPATH, f"//span[contains(text(),'测试')]").click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'编辑')]").click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='30']").clear()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='30']").send_keys("测试1")
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'提交')]").click()
        sleep(1)
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'编辑')]").click()
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'管理员权限')]").click()
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'指定管理员')]").click()
        # self.drvier.find_elements(By.XPATH, "//img[@class='pointAtGroup-icon']")[0].click()
        # self.drvier.find_element(By.XPATH, "//div[contains(text(),'admin')]").click()
        # self.drvier.find_element(By.XPATH,
        #                     "//*[@id='pane-second']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        listbtn = self.drvier.find_elements(By.XPATH, '//a[@target="_blank"]/span')[0]
        style = self.drvier.find_elements(By.CSS_SELECTOR, '.button.level0.switch.noline_close')
        if len(style) > 0:
            sleep(2)
            listbtn.click()
            self.itembank_edit_teacher()
        else:
            self.itembank_edit_teacher()

    def itembank_edit_teacher(self):
        #编辑教员
        self.drvier.find_element(By.XPATH, f"//span[contains(text(),'测试1')]").click()
        sleep(3)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'编辑')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'教员权限')]").click()
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'指定教员')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//*[@id='pane-third']/div[1]/div/div[2]/div/div[2]/div[1]/img").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'test1')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH,
                            "//*[@id='pane-third']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
        self.drvier.find_element(By.XPATH, "//*[@id='pane-third']/div[2]/button[1]/span").click()
        return ('测试1')


    def add_topic(self,test):
        #试题库新增题目
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'题目')]")[2].click()
        self.drvier.find_element(By.XPATH,"//div[@data-placeholder='题干最长字数不能超过500']").send_keys(test)
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"][@maxlength="200"]')[0].send_keys("1")
        self.drvier.find_elements(By.XPATH, '//input[@class="el-input__inner"][@maxlength="200"]')[1].send_keys("1")
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'提交')]")[0].click()
        return ()

    def import_data(self):
        #试题库导入题目
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'导入题目')]").click()
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/paper-question_cn.xls")
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()

    def itembank_edit_details(self):
        # 试题库功能操作
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='编辑']")[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH,"//div[@data-placeholder='题干最长字数不能超过500']").send_keys("ceshi")
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'提交')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='查看']")[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//button[@aria-label="Close"]')[2].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='归档']")[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='删除']")[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//label[@class="el-checkbox"]')[1].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'删除')]")[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        return ('test_picture+1')

    def pigeonhole(self):
        #试题库批量归档
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'归档')]")[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        return ()

    def itembank_file_operate_details(self):
        #已归档操作
        sleep(1)
        self.drvier.find_element(By.XPATH, '//div[@id="tab-one-file"]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='查看']")[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//div[@aria-label="查看题目"]/div/button[@aria-label="Close"]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='删除']")[1].click()
        sleep(2)
        self.drvier.find_element(By.XPATH,"//span[contains(text(),'确认')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='激活']")[0].click()
        sleep(1)

        # self.drvier.find_element(By.CSS_SELECTOR, '#pane-second .el-table__body tr:nth-child(1) label>span').click()
        self.drvier.find_elements(By.XPATH,
                                 '//td[@rowspan="1"]//span[@class="el-checkbox__input"]')[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'激活')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//label[@class="el-checkbox"]')[1].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'删除')]")[2].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()


    def empty_topic(self):
        #清空试题库内容及删除分类
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'清空题目')]")[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH,
                                 '//*[@id="pane-one-file"]/div/div[@class="el-dialog__wrapper"]/div/div[@class="el-dialog__footer"]/span/button[2]/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//div[@id="tab-one"]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'清空题目')]")[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,
                                 '//div[@role="dialog"][@class="el-dialog"]/div[@class="el-dialog__footer"]//button[2]')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"测试1")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[@class="txt"][contains(text(),"删除")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '/html/body/div[@class="el-dialog__wrapper"]/div/div[@class="el-dialog__footer"]/span/button[2]/span').click()
        return ()

    def test_add_testpaer(self,headline):
        #新增试卷
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//span[contains(text(),"新增")]')[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys(headline)
        self.drvier.find_element(By.XPATH,'//input[@aria-valuemax="200"]').clear()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//input[@aria-valuemax="200"]').send_keys("30")
        sleep(1)
        element = self.drvier.find_element(By.XPATH, '//input[@type="radio"][@value="QUESTION"]')
        self.drvier.execute_script("arguments[0].click();", element)
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[contains(text(),"保存")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"添加抽题规则")]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//span[@class="el-input__suffix-inner"]/i[@class="el-icon-arrow-right"]')[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//a[@target="_blank"]/span')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//a[@title="军事目录"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//div[@aria-label="请选择"]//span/button[2]/span').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//input[@max="Infinity"]')[3].send_keys("1")
        self.drvier.find_elements(By.XPATH, '//input[@max="Infinity"]')[4].send_keys("1")
        self.drvier.find_element(By.XPATH,'//i[@title="保存"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'试卷库')]").click()
        return ()

    def testpaper_edit_details(self):
        #操作编辑内容
        self.drvier.find_elements(By.XPATH,'//img[@title="编辑"]')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'试卷库')]").click()
        listbtn = self.drvier.find_elements(By.XPATH, '//a[@target="_blank"]/span')[0]
        style = self.drvier.find_elements(By.CSS_SELECTOR, '.button.level0.switch.noline_close')
        if len(style) > 0:
            sleep(2)
            listbtn.click()
            self.testpaer_operate()
        else:
            self.testpaer_operate()

    def testpaer_operate(self):
        #操作内容
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//img[@title="删除"]')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH,
                                 '/html/body/div[@class="el-dialog__wrapper"]/div/div[@class="el-dialog__footer"]/span/button[2]/span').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//div[@title="归档"]')[0].click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')[1].click()
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'删除')]")[1].click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        self.drvier.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')[0].click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'归档')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        return ()


    def testpaer_file_operate_details(self):
        #已归档试卷操作及删除
        self.drvier.find_element(By.XPATH, '//div[@id="tab-second"]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//div[@title="查看"]')[0].click()
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'试卷库')]").click()
        listbtn = self.drvier.find_elements(By.XPATH, '//a[@target="_blank"]/span')[0]
        style = self.drvier.find_elements(By.CSS_SELECTOR, '.button.level0.switch.noline_close')
        if len(style) > 0:
            sleep(2)
            listbtn.click()
            self.testpaer_file_delete()
        else:
            self.testpaer_file_delete()


    def testpaer_file_delete(self):
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//div[@id="tab-second"]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//div[@title="激活"]')[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//table/thead/tr/th[1]/div/label/span')[1].click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'激活')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//div[@id="tab-first"]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//span[@class="el-checkbox__inner"]')[0].click()

        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'删除')]")[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_element(By.XPATH, "//span[@class='txt'][contains(text(),'删除')]").click()
        self.drvier.find_element(By.XPATH,'/html/body/div[@class="el-dialog__wrapper"]/div/div[@class="el-dialog__footer"]/span/button[2]/span').click()
        return ()

    def certificate_edit_classify(self):
        # 证书分类编辑
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试')]").click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'编辑')]").click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='30']").clear()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='30']").send_keys("测试1")
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'提交')]").click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'管理员权限')]").click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'指定管理员')]").click()
        self.drvier.find_elements(By.XPATH, "//img[@class='pointAtGroup-icon']")[0].click()
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'admin')]").click()
        self.drvier.find_element(By.XPATH,
                                 "//*[@id='pane-second']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
        return()

    def add_certificate_template(self,name):
        #新增证书模板
        sleep(1)
        self.drvier.find_element(By.XPATH,"//span[contains(text(),'+证书模板')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,"//input[@maxlength='30']")[0].send_keys(name)

        self.drvier.find_element(By.XPATH, '//span[contains(text(),"保存")]').click()
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"返回")]').click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()

        return ()

    def certificate_template_edit_details(self):
        #证书模板编辑
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//img[@title="编辑"]')[0].click()
        sleep(1)
        # self.drvier.find_elements(By.XPATH, "//input[@maxlength='30']")[0].send_keys("测试2")
        # self.drvier.find_element(By.XPATH, '//span[contains(text(),"保存")]').click()
        # self.drvier.find_element(By.XPATH, '//span[contains(text(),"返回")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//div[@id="tab-fourth"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"设置模板")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//div[contains(text(),"背景图")]').click()
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"添加图片")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//input[@id="uploads"]').send_keys('D:/dvieo/test_picture.jpeg')
        sleep(1)
        self.drvier.find_element(By.XPATH,'//*[@id="pane-fourth"]/div/div/div[2]/div/div[2]/div[2]/span/button[2]/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//div[contains(text(),"添加到预览区")]').click()
        self.drvier.find_element(By.XPATH,'//div[contains(text(),"头像")]').click()
        head_portrait =self.drvier.find_element(By.XPATH,'//div[@id="1view_view"]')
        action_chains = ActionChains(self.drvier)
        action_chains.click_and_hold(head_portrait).perform()
        action_chains.drag_and_drop_by_offset(head_portrait, 126, 180).perform()
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"制作完成")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//input[@type="text"][@class="tem_title"]').send_keys("测试1")
        self.drvier.find_element(By.XPATH,'//*[@id="pane-fourth"]/div/div/div[2]/div/div[2]/div[2]/span/button[2]/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"模板库")]').click()
        self.drvier.find_element(By.XPATH, '//div[contains(text(),"测试1")]').click()
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"引用模板")]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//span[contains(text(),"返回")]')[1].click()




    def certificate_template_delete(self):
        #证书模板删除及分类删除
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//img[@title="删除"]')[0].click()
        self.drvier.find_element(By.XPATH,'/html/body/div[@class="el-dialog__wrapper"]/div/div[@class="el-dialog__footer"]/span/button[2]/span').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//span[@class="el-checkbox__inner"]')[0].click()
        self.drvier.find_elements(By.XPATH, '//span[contains(text(),"删除")]')[1].click()
        self.drvier.find_element(By.XPATH, '/html/body/div[@aria-label="提示"]/div/div[@class="el-message-box__btns"]/button[2]/span').click()
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"测试1")]').click()
        self.drvier.find_element(By.XPATH, '//span[@class="txt"][contains(text(),"删除")]').click()
        self.drvier.find_element(By.XPATH,'//div[@role="dialog"]/div[3]/span/button[2]').click()



    def add_knowledge_label(self,name):
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//span[contains(text(),"添加")]')[0].click()
        sleep(1)
        self.drvier.find_element(By.CSS_SELECTOR,'.el-select__caret.el-input__icon.el-icon-arrow-up').click()
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"有效")]').click()
        self.drvier.find_element(By.XPATH,'//input[@maxlength="255"]').send_keys(name)
        self.drvier.find_elements(By.XPATH, '//span[contains(text(),"保存")]')[0].click()

    def operate_knowledge_label(self):
        self.drvier.find_elements(By.XPATH,'//img[@title="编辑"]')[0].click()
        self.drvier.find_element(By.XPATH,'//input[@maxlength="255"]').send_keys("ceshi")
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"保存")]').click()
        self.drvier.find_elements(By.XPATH, '//div[@title="查看"]')[0].click()
        self.drvier.find_elements(By.XPATH, '//span[contains(text(),"返回")]')[0].click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_elements(By.XPATH, '//img[@title="删除"]')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//div[@role="dialog"]/div[3]/span/button[2]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//thead[@class="has-gutter"]//div[@class="cell"]')[0].click()
        self.drvier.find_elements(By.XPATH, '//span[contains(text(),"删除")]')[1].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//div[@role="dialog"]/div[3]/span/button[2]')[1].click()
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"测试1")]').click()
        self.drvier.find_element(By.XPATH, '//span[@class="txt"][contains(text(),"删除")]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//div[@role="dialog"]/div[3]/span/button[2]')[2].click()
