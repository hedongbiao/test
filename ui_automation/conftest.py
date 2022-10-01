# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from time import sleep
#登录



# @pytest.fixture(scope='session')
# def loin():
#     drvier = webdriver.Chrome()
#
#     drvier.get("http://8.134.109.213:8079/login")
#     drvier.find_element(By.XPATH,"//input[@type='text']").send_keys("admin")
#     drvier.find_element(By.XPATH,"//input[@type='password']").send_keys("123456")
#     drvier.find_element(By.XPATH,"//button[@type='button']").click()
#     drvier.implicitly_wait(3)
#     return drvier
@pytest.fixture()
def edit_classify():
    # 知识点分类编辑
    drvier = find_element(By.XPATH, "//span[contains(text(),'测试')]").click()
    drvier.find_element(By.XPATH, "//span[contains(text(),'测试')]").click()
    drvier.find_element(By.XPATH, "//span[contains(text(),'编辑')]").click()
    drvier.find_element(By.XPATH, "//input[@maxlength='30']").clear()
    drvier.find_element(By.XPATH, "//input[@maxlength='30']").send_keys("测试1")
    drvier.find_element(By.XPATH, "//span[contains(text(),'提交')]").click()
    drvier.find_element(By.XPATH, "//span[contains(text(),'管理员权限')]").click()
    drvier.find_element(By.XPATH, "//span[contains(text(),'指定管理员')]").click()
    drvier.find_elements(By.XPATH, "//img[@class='pointAtGroup-icon']")[0].click()
    drvier.find_element(By.XPATH, "//div[contains(text(),'admin')]").click()
    drvier.find_element(By.XPATH,
                             "//*[@id='pane-second']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
    drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
    sleep(1)
    drvier.find_element(By.XPATH, "//span[contains(text(),'教员权限')]").click()
    sleep(2)
    drvier.find_element(By.XPATH, "//span[contains(text(),'指定教员')]").click()
    sleep(1)
    drvier.find_element(By.XPATH, "//*[@id='pane-third']/div[1]/div/div[2]/div/div[2]/div[1]/img").click()
    sleep(1)
    drvier.find_element(By.XPATH, "//div[contains(text(),'test006')]").click()
    sleep(1)
    drvier.find_element(By.XPATH,
                             "//*[@id='pane-third']/div[1]/div/div[4]/div[1]/div/div[3]/span/button[2]").click()
    drvier.find_element(By.XPATH, "//*[@id='pane-third']/div[2]/button[1]/span").click()





