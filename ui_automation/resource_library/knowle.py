

"""资源库"""
from typing import List

from selenium.webdriver.common.by import By

from time import sleep
from shangxue.ui_automation.base_page import BasePage
from shangxue.ui_automation.resource_library.knowledge_classify import KnowledgeClassify



class Knowle(BasePage):


    # def ification_on(self):
    #     sleep(1)
    #     self.drvier.find_elements(By.XPATH, '//span[@class="node_name"]')[0].click()
    #     listbtn = self.drvier.find_elements(By.XPATH, '//a[@target="_blank"]/span')[0]
    #     style = self.drvier.find_elements(By.CSS_SELECTOR, '.button.level0.switch.noline_close')
    #     if len(style) > 0:
    #         sleep(1)
    #         listbtn.click()
    #         return KnowledgeClassify(self.drvier)
    #     else:
    #         return KnowledgeClassify(self.drvier)

    def knowle(self):
        #知识点

        sleep(1)
        zsd = self.drvier.find_element(By.XPATH, "//span[contains(text(),'知识点')]")
        zsd.click()
        self.ification_on()
        return KnowledgeClassify(self.drvier)
        # listbtn = self.drvier.find_element(By.XPATH, '//a[@title="所有知识点分类"]/span[1]')
        # listbtn.click()
        # sleep(2)
        # js = "document.querySelector('.level0>a>span:nth-child(1)').className='button level0 switch noline_open';document.querySelector('.level0>a>span:nth-child(2)').className='button ico_open';document.querySelector('.level0>ul').style.display='inline'"
        # self.drvier.execute_script(js)
        # return KnowledgeClassify(self.drvier)
        # listbtn.click()
        # sleep(2)
        # style:List = self.drvier.find_elements(By.CSS_SELECTOR,'.level0>ul[style="display: none;"]')
        # sleep(2)
        # if len(style) > 0:
        #     listbtn.click()
        #     return KnowledgeClassify(self.drvier)
        # else:
        #     return KnowledgeClassify(self.drvier)



    def law(self):
        #法律法规
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'法律法规')]").click()
        sleep(1)
        self.ification_on()
        return KnowledgeClassify(self.drvier)


    def case(self):
        #案例
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'案例')]").click()
        self.ification_on()
        return KnowledgeClassify(self.drvier)

    def itrmbank(self):
        #试题库
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'试题库')]").click()
        self.ification_on()
        return KnowledgeClassify(self.drvier)


    def test_paper_warehouse(self):
        #试卷库
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'试卷库')]").click()
        self.ification_on()
        return KnowledgeClassify(self.drvier)

    def certificate_template(self):
        #证书模板管理
        sleep(1)
        self.drvier.find_element(By.XPATH, '//div[@class="ellipsis"] [contains(text(),"证书模板管理")]').click()
        self.ification_on()
        return KnowledgeClassify(self.drvier)

    def knowledge_label(self):
        #知识点标签
        sleep(1)
        self.drvier.find_element(By.XPATH, '//div[@class="ellipsis"] [contains(text(),"知识标签管理")]').click()
        self.ification_on()
        return KnowledgeClassify(self.drvier)

    def classify(self):
        #分类名称
        sleep(1)
        self.drvier.find_elements(By.XPATH, '//span[@class="node_name"]')[0].click()
        sleep(1)
        listbtn = self.drvier.find_elements(By.XPATH, '//a[@target="_blank"]/span')[0]
        style = self.drvier.find_elements(By.CSS_SELECTOR, '.button.level0.switch.noline_close')
        if len(style) > 0:
            sleep(1)
            listbtn.click()
            self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
            return KnowledgeClassify(self.drvier)
        else:
            self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
            return KnowledgeClassify(self.drvier)
        # sleep(2)
        # style: List = self.drvier.find_elements(By.CSS_SELECTOR, '.level0>ui[style="display: none;"]')
        # sleep(2)
        # if len(style) > 0:
        #     listbtn.click()
        #     self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        #     return KnowledgeClassify(self.drvier)
        # else:
        #     self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        #     return KnowledgeClassify(self.drvier)




    def test(self):
        sleep(1)
        self.drvier.find_element(By.XPATH, "//div[contains(text(),'证书模板管理')]").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH,'//a[@target="_blank"]/span')[0].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        return KnowledgeClassify(self.drvier)