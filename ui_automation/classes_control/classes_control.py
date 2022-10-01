# -*- coding:utf-8 -*-
"""班次管理"""
from time import sleep

from selenium.webdriver.common.by import By

from shangxue.ui_automation.base_page import BasePage


class ClassdesControl(BasePage):

    def click_add(self):
        #内容添加时点击操作
        self.drvier.find_element(By.XPATH, '//div[@class="el-dropdown"]/button/span/i').click()

    def click_submit(self):
        #内容提交操作
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'提交')]").click()

    def click_keep(self):
        #内容保存操作
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()

    def add_classify(self,name):
        # 分类新增
        sleep(2)
        self.find(By.XPATH,'//div[@id="container"]/div/li/a').click()
        self.find(By.XPATH, "//span[contains(text(),'添加')]").click()
        self.find(By.XPATH, "//input[@maxlength='30']").send_keys(name)
        self.click_submit()
        return ('测试')


    def edit_classify(self,name,edit_name):
        # 分类编辑
        sleep(1)
        self.find(By.XPATH, f"//span[text() = '{name}']").click()
        self.find(By.XPATH, "//span[contains(text(),'编辑')]").click()
        self.find(By.XPATH, "//input[@maxlength='30']").clear()
        self.find(By.XPATH, "//input[@maxlength='30']").send_keys(edit_name)
        self.click_submit()
        sleep(1)
        self.find(By.XPATH, "//span[contains(text(),'管理员权限')]").click()
        self.find(By.XPATH, "//span[contains(text(),'指定管理员')]").click()
        self.finds(By.XPATH, "//img[@class='pointAtGroup-icon']")[0].click()
        self.find(By.XPATH, "//div[contains(text(),'admin')]").click()
        self.find(By.XPATH,
                            "//*[@id='pane-second']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
        self.click_keep()

        return ('测试1')

    def add_classes(self,name,headline,target,trainee):
        #新增班次
        sleep(1)
        self.find(By.XPATH, f"//span[text() = '{name}']").click()
        sleep(2)
        self.finds(By.XPATH,'//div[@class="operation"]/button')[0].click()
        self.find(By.XPATH,'//input[@maxlength="50"]').send_keys(headline)
        self.finds(By.XPATH,'//div[@class="quill-editor"]/div[2]/div')[0].send_keys(target)
        sleep(1)
        self.finds(By.XPATH, '//div[@class="quill-editor"]/div[2]/div')[3].send_keys(trainee)
        self.click_keep()
        sleep(1)
        return ()


    def add_classes_details(self,name,teacher):
        #新增课程
        sleep(1)
        self.find(By.XPATH, "//span[contains(text(),'内容')]").click()
        self.find(By.XPATH, "//span[contains(text(),'添加课程')]").click()
        sleep(1)
        self.finds(By.XPATH, '//input[@class="el-input__inner"]')[1].send_keys(name)
        self.find(By.XPATH, '//div[@class="pointAtGroup-search"]').click()
        self.find(By.XPATH, f'//div[@class="cell"][contains(text(),"{teacher}")]').click()
        self.find(By.XPATH, '//div[@aria-label="请选择"]/div[3]/span/button[2]').click()
        self.click_keep()
        return ()

    def add_classes_details_drill(self,drill_name,nade_name):
        #新增课程内容
        sleep(1)
        self.click_add()
        sleep(1)
        self.find(By.XPATH,'//span[@class="icon_size"][text() = "训练专题"]').click()
        sleep(1)
        self.find(By.XPATH,'//input[@maxlength="50"]').send_keys(drill_name)
        self.finds(By.XPATH,'//div[@class="tree-depart-add"]/i[@class="iconfont"]')[0].click()
        self.find(By.XPATH,f'//span[@class="node_name"][text() = "{nade_name}"]').click()
        self.finds(By.XPATH,'//div[@class="el-dialog"]/div[@class="el-dialog__footer"]/span/button[2]')[1].click()
        sleep(1)
        self.click_keep()
        return ()

    def add_section(self,section_name,teacher):
        #新增课程章节
        sleep(1)
        self.find(By.XPATH, "//span[contains(text(),'添加章节')]").click()
        sleep(1)
        self.finds(By.XPATH, '//input[@class="el-input__inner"]')[1].send_keys(section_name)
        self.find(By.XPATH, '//div[@class="pointAtGroup-search"]').click()
        self.find(By.XPATH, f'//div[@class="cell"][contains(text(),"{teacher}")]').click()
        self.find(By.XPATH, '//div[@aria-label="请选择"]/div[3]/span/button[2]').click()
        self.click_keep()
        return ()

    def add_section_quote_laws(self,name):
        #引用类
        sleep(1)
        self.click_add()
        sleep(1)
        self.finds(By.XPATH, f'//span[@class="icon_size"][text() = "{name}"]')[1].click()
        sleep(1)
        self.finds(By.XPATH,'//div[@aria-label="添加课件"]//label[@class="el-checkbox"]/span')[2].click()
        sleep(1)
        zsd = self.finds(By.XPATH,"//span[contains(text(),'确认添加')]")[1]
        zsd.click()
        sleep(1)
        self.finds(By.XPATH,'//div[@aria-label="编辑内容"]//label[@class="el-checkbox"]/span')[0].click()
        self.find(By.XPATH,"//div[@aria-label='编辑内容']//span[contains(text(),'保存')]").click()
        return ()


    def add_section_video(self,name,add_name,file):
        #添加类
        sleep(1)
        self.click_add()
        sleep(1)
        self.finds(By.XPATH, f'//span[@class="icon_size"][text() = "{name}"]')[1].click()
        sleep(1)
        self.find(By.XPATH, '//input[@maxlength="50"]').send_keys(add_name)
        self.find(By.XPATH,
                                 '//span[contains(text(),"上传文件")]/preceding-sibling::span[@class="el-radio__input"]').click()
        self.find(By.XPATH,'//input[@class="el-upload__input"]').send_keys(file)
        sleep(2)
        self.click_keep()
        return ()


    def add_scenario_task(self,task_headline,file,teacher):
        #新增想定作业
        sleep(1)
        self.click_add()
        sleep(1)
        self.finds(By.XPATH, '//span[@class="icon_size"][text() = "新建想定作业"]')[1].click()
        sleep(1)
        self.find(By.XPATH, '//div[@aria-label="添加作业"]/div[3]/span/button[2]').click()
        sleep(1)
        self.find(By.XPATH, '//input[@maxlength="50"]').send_keys(task_headline)
        self.find(By.XPATH, '//input[@class="el-upload__input"]').send_keys(file)
        sleep(2)
        self.find(By.XPATH,'//div[@id="tab-second"]').click()
        sleep(1)
        self.find(By.XPATH, "//span[contains(text(),'文本')]").click()
        sleep(1)
        self.find(By.XPATH,'//div[@id="tab-third"]').click()
        sleep(1)
        self.find(By.XPATH,'//div[@class="pointAtGroup-search"]').click()
        sleep(1)
        self.find(By.XPATH, f'//div[@class="cell"][contains(text(),"{teacher}")]').click()
        sleep(1)
        self.find(By.XPATH,'//div[@aria-label="请选择"]/div[3]/span/button[2]').click()
        self.click_keep()
        sleep(1)
        self.find(By.XPATH, "//span[contains(text(),'返回')]").click()
        return ()


    def add_freedom_drill(self,drill_headline,test):
        #新增自主训练
        sleep(1)
        self.click_add()
        sleep(1)
        self.finds(By.XPATH, '//span[@class="icon_size"][text() = "新建自主训练"]')[1].click()
        self.find(By.XPATH, '//input[@maxlength="50"]').send_keys(drill_headline)
        self.click_keep()
        sleep(1)
        self.find(By.XPATH, "//span[text() = '题库']").click()
        self.find(By.XPATH,'//div[@class="btn-w"]/button[2]').click()
        sleep(1)
        self.find(By.XPATH, "//div[@data-placeholder='题干最长字数不能超过500']").send_keys(test)
        sleep(1)
        self.finds(By.XPATH, '//input[@class="el-input__inner"][@maxlength="200"]')[0].send_keys("1")
        self.finds(By.XPATH, '//input[@class="el-input__inner"][@maxlength="200"]')[1].send_keys("1")
        self.click_keep()


    def add_subject_discuss(self):
        sleep(1)
        self.click_add()
        sleep(1)
        self.finds(By.XPATH,'//span[@class="icon_size"][text() = "新建主题研讨"]')[1].click()
        sleep(1)
        self.find(By.XPATH, '//div[@aria-label="添加作业"]/div[3]/span/button[2]').click()
        self.find(By.XPATH,'//label[contains(text(),"标题")]/following-sibling::div[1]').send_keys()

