# -*- coding:utf-8 -*-
"""用户管理"""
from time import sleep

from selenium.webdriver.common.by import By

from shangxue.ui_automation.base_page import BasePage
from shangxue.ui_automation.user_control.user_classify import UserClassify

class UserModuel(BasePage):

    def professional_management(self):
        #专业模块管理
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//div[@class="ellipsis"]')[0].click()
        sleep(1)
        self.ification_on()
        return UserClassify(self.drvier)

    def post_management(self):
        #岗位管理
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//div[@class="ellipsis"]')[1].click()
        sleep(1)
        self.ification_on()
        return UserClassify(self.drvier)

    def user_management(self):
        #用户管理
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//div[@class="ellipsis"]')[2].click()
        sleep(1)
        self.ification_on()
        return UserClassify(self.drvier)