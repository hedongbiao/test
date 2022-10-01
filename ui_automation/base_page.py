# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pymysql

import pytest
#登录



class BasePage():

    def __init__(self,base_drvier:WebDriver = None):
        if base_drvier == None:
            self.drvier = webdriver.Chrome()
            self.drvier.get("")
            self.drvier.find_element(By.XPATH,"//input[@type='text']").send_keys("")
            self.drvier.find_element(By.XPATH,"//input[@type='password']").send_keys("")
            self.drvier.find_element(By.XPATH,"//button[@type='button']").click()
            self.drvier.maximize_window()
            self.drvier.implicitly_wait(3)


        else:
            self.drvier = base_drvier


    def teardown_module(self):
        self.drvier.quit()

    def ification_on(self):
        #判断分类是否展开
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//span[@class="node_name"]')[0].click()
        listbtn = self.drvier.find_elements(By.XPATH, '//a[@target="_blank"]/span')[0]
        style = self.drvier.find_elements(By.CSS_SELECTOR, '.button.level0.switch.noline_close')
        if len(style) > 0:
            sleep(1)
            listbtn.click()
            return BasePage(self.drvier)
        else:
            return BasePage(self.drvier)

    def find(self,by,locator):

        return self.drvier.find_element(by=by,value=locator)


    def finds(self,by,locator):

        return self.drvier.find_elements(by=by,value=locator)