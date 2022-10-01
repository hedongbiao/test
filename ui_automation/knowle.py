

#知识点
from selenium.webdriver.common.by import By

from time import sleep
from ui_automation.base_page import BasePage
from ui_automation.resource import Rwsource


class Knowled(Rwsource):

    def knowledge(self):
        from ui_automation.test_resource.test_resource_library import TestResoueceLibrary
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'知识点')]").click()

        return TestResoueceLibrary()