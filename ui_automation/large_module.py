

"""首页"""
from selenium.webdriver.common.by import By

from shangxue.ui_automation.base_page import BasePage
from time import sleep
from shangxue.ui_automation.resource_library.knowle import Knowle
from shangxue.ui_automation.user_control.user_moduel import UserModuel
from shangxue.ui_automation.classes_control.classes_control import ClassdesControl
from shangxue.ui_automation.knowledge_contest.theme_list import ThemeList

class LargeModule(BasePage):

    def rwsource(self):
        """资源库"""

        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'资源库')]").click()
        return Knowle(self.drvier)

    def user_control(self):
        """学员管理"""
        sleep(1)
        element = self.drvier.find_element(By.XPATH, "//span[contains(text(),'学员管理')]")
        self.drvier.execute_script("arguments[0].click();", element)
        # self.drvier.find_element(By.XPATH, "//span[contains(text(),'学员管理')]").click()
        return UserModuel(self.drvier)

    def knowledge_Contest(self):
        """知识比武"""
        sleep(1)
        element = self.drvier.find_element(By.XPATH, "//span[contains(text(),'知识比武')]")
        self.drvier.execute_script("arguments[0].click();", element)
        return ThemeList(self.drvier)

    def classes_control(self):
        """班次管理"""
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'班次管理')]").click()
        return ClassdesControl(self.drvier)

