# -*- coding:utf-8 -*-
"""用户管理"""
from time import sleep

from selenium.webdriver.common.by import By

from shangxue.ui_automation.base_page import BasePage

class UserClassify(BasePage):



    def add_professional_management(self,serial_number,headline):
        #新增专业模块
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[@class="txt"][contains(text(),"新增")]').click()
        self.drvier.find_elements(By.XPATH, '//input[@class="el-input__inner"]')[0].send_keys(serial_number)
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"]')[1].send_keys(headline)
        self.drvier.find_element(By.XPATH,'//div[@class="tree-depart-add"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[@id="treeDialog_1_check"]').click()
        self.drvier.find_element(By.XPATH,'//div[@aria-label="请选择"]/div[3]/span/button[2]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[contains(text(),"提交")]').click()
        return ()

    def edit_classify(self,headline):
        #编辑分类
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[text() = "测试"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[@class="txt"][contains(text(),"编辑")]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"]')[1].clear()
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"]')[1].send_keys(headline)
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"提交")]').click()
        return ()

    def delete_professional_management(self,name):
        #删除专业模块
        sleep(1)
        self.drvier.find_element(By.XPATH,f'//span[@class="node_name"][text() = "{name}"]').click()
        self.drvier.find_element(By.XPATH,'//span[@class="txt"][contains(text(),"删除")]').click()
        self.drvier.find_element(By.XPATH,'//div[@aria-label="提示"]/div[3]/span/button[2]').click()
        return ()

    def add_post(self,serial_number,headline):
        #新增岗位管理
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[@class="txt"][contains(text(),"新增")]').click()
        self.drvier.find_elements(By.XPATH, '//input[@class="el-input__inner"]')[0].send_keys(serial_number)
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"]')[1].send_keys(headline)
        self.drvier.find_elements(By.XPATH,'//div[@class="tree-depart-add"]')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//a[@id="treeDialog_1_a"]').click()
        self.drvier.find_element(By.XPATH,'//div[@aria-label="请选择所有岗位"]/div[3]/span/button[2]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//div[@class="tree-depart-add"]')[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, '//span[@id="treeDialog_1_span"]').click()
        self.drvier.find_element(By.XPATH, '//div[@aria-label="请选择所有专业模块"]/div[3]/span/button[2]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[contains(text(),"提交")]').click()
        return ()

    def delete_post(self,name):
        #删除岗位管理
        sleep(1)
        self.drvier.find_element(By.XPATH,f'//span[@class="node_name"][text() = "{name}"]').click()
        self.drvier.find_element(By.XPATH,'//span[@class="txt"][contains(text(),"删除")]').click()
        self.drvier.find_element(By.XPATH,'//div[@aria-label="提示"]/div/div[3]/button[2]').click()
        return ()

    def add_user(self,name,account,role):
        #新增用户
        sleep(1)
        self.drvier.find_element(By.XPATH,f'//span[@class="node_name"][text() = "{name}"]').click()
        self.drvier.find_element(By.XPATH,'//i[@class="el-icon-plus"]').click()
        sleep(2)
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"]')[0].send_keys(account)
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"]')[1].send_keys("123456")
        self.drvier.find_elements(By.XPATH,'//input[@class="el-input__inner"]')[2].send_keys(account)
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//i[@class="iconfont"]')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH,f'//span[@class="node_name"] [text() ="{name}"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//div[@aria-label="请选择"]/div[3]/span/button[2]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,f'//span[text() = "{role}"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'//span[contains(text(),"提交")]').click()
        return ()



    def edit_user(self,name,password,account):
        #编辑用户
        self.drvier.find_element(By.XPATH,f'//span[@class="node_name"][text() = "{name}"]').click()
        self.drvier.find_elements(By.XPATH,'//img[@title="修改密码"]')[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//input[@type="password"]')[0].send_keys(password)
        self.drvier.find_elements(By.XPATH, '//input[@type="password"]')[1].send_keys(password)
        self.drvier.find_element(By.XPATH,'//div[@aria-label="设置新密码"]/div[3]/span/button[2]').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//img[@title="修改用户"]')[0].click()
        self.drvier.find_elements(By.XPATH, '//input[@class="el-input__inner"]')[2].clear()
        self.drvier.find_elements(By.XPATH, '//input[@class="el-input__inner"]')[2].send_keys(account)
        self.drvier.find_element(By.XPATH, '//span[contains(text(),"提交")]').click()
        return ()

    def del_user(self,name):
        #删除用户
        self.drvier.find_element(By.XPATH, f'//span[@class="node_name"][text() = "{name}"]').click()
        self.drvier.find_elements(By.XPATH, '//img[@title="删除用户"]')[0].click()
        self.drvier.find_element(By.XPATH,'//div[@aria-label="提示"]/div[3]/span/button[2]').click()
        return ()