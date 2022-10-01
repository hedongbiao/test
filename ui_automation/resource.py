

#首页
from selenium.webdriver.common.by import By

from ui_automation.base_page import BasePage
from time import sleep


class Rwsource(BasePage):

    def rwsource(self):
        from ui_automation.knowle import Knowled
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'资源库')]").click()
        return Knowled()
