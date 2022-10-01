# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By





class TestResoueceLibrary():

    def test_knowledge_add_classify(self):
        #知识点分类新增
        from ui_automation.knowle import Knowled

        test=Knowled()
        test.knowledge()
        self.drvier.find_element(By.XPATH,"//span[contains(text(),'新增')]").click()
        self.drvier.find_element(By.XPATH,"//input[@maxlength='30']").send_keys("测试")
        self.drvier.find_element(By.XPATH,"//span[contains(text(),'提交')]").click()

    def test_edit(self,test_knowledge_edit_classify):
        self.drvier = test_knowledge_edit_classify

 
    def test_knowledge_add_video(self):
        #新增视频
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'视频')]").click()
        self.drvier.find_element(By.XPATH,"//input[@maxlength='50']").send_keys("test_vudeo")
        self.drvier.find_element(By.XPATH,'//input[@type="file"]').send_keys("C:/Users/Administrator/Videos/Captures/f3bbbf14b545e9366dc9e39daef0c2f8.mp4")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()

    def test_knowledge_add_office(self):
        #新增office
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_elements(By.XPATH,"//button[@type='button']")[3].click()
        self.drvier.find_element(By.XPATH,"//input[@maxlength='50']").send_keys("test_office")
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_office.xls")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
    def test_knowledge_add_pdf(self):
        #新增pdf
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_elements(By.XPATH, "//button[@type='button']")[4].click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("test_pdf")
        sleep(1)
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_pdf.pdf")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
       

    def test_knowledge_add_audio(self):
        #添加音频
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_elements(By.XPATH, "//button[@type='button']")[5].click()
        sleep(2)
        self.drvier.find_elements(By.XPATH, "//i[@class='el-icon-plus']")[6].click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("test_audio")
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_audio.mp3")
        sleep(3)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()

    def test_knowledge_add_picture(self):
        #添加视频
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_elements(By.XPATH, "//button[@type='button']")[5].click()
        sleep(2)
        self.drvier.find_elements(By.XPATH, "//i[@class='el-icon-plus']")[7].click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("test_picture")
        self.drvier.find_element(By.XPATH, '//input[@type="file"]').send_keys("D:/dvieo/test_picture.jpeg")
        sleep(2)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
    
    def test_knowledge_edit(self):
        #编辑知识点
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        self.drvier.find_elements(By.XPATH,"//img[@title='编辑']")[0].click()
        self.drvier.find_element(By.XPATH, "//input[@maxlength='50']").send_keys("test_picture+1")
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'保存')]").click()
  
    def test_knowledge_operate(self):
        #所有知识点操作
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
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
        self.drvier.find_element(By.XPATH,'//i[@class="iconfont"]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'确认')]").click()

    def test_knowledge_file_operate(self):
        #已归档知识点操作
        self.drvier.find_element(By.XPATH, "//span[contains(text(),'测试1')]").click()
        sleep(1)
        self.drvier.find_element(By.XPATH,"//div[@id='tab-second']").click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='查看']")[5].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//button[@aria-label='Close']")[5].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//img[@title='删除']")[5].click()
        sleep(1)
        self.drvier.find_element(By.CSS_SELECTOR, 'body>div:nth-child(9)>div>div.el-dialog__footer button:nth-child(2)').click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//div[@title='激活']")[0].click()
        sleep(1)

        #self.drvier.find_element(By.CSS_SELECTOR, '#pane-second .el-table__body tr:nth-child(1) label>span').click()
        self.drvier.find_element(By.XPATH,'//*[@id="pane-second"]//*[@class="el-table__body"]//tr[1]//label/span').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,"//span[contains(text(),'激活')]").click()
        sleep(1)

    def test_knowledge_dilite(self):
        #删除知识点及分类
        self.drvier.find_element(By.XPATH,'//*[@id="pane-second"]//table[@class="el-table__header"]//tr[1]//label/span').click()
        self.drvier.find_element(By.XPATH,'//*[@id="pane-second"]//span[contains(text(),"删除")]').click()
        self.drvier.find_element(By.XPATH,"//*[@id='admin']/div[2]/div/div[6]/div/div[3]/span/button[2]/span").click()
        self.drvier.find_element(By.XPATH, "//div[@id='tab-first']").click()
        self.drvier.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')[0].click()
        sleep(1)
        self.drvier.find_elements(By.XPATH, "//span[contains(text(),'删除')]")[1].click()
        sleep(1)
        self.drvier.find_element(By.XPATH, "//*[@id='admin']/div[2]/div/div[6]/div/div[3]/span/button[2]/span").click()
        self.drvier.find_element(By.XPATH,'//span[@class="txt"][contains(text(),"删除")]').click()
        sleep(1)
        self.drvier.find_element(By.XPATH,'/html/body/div[5]/div/div[3]/span/button[2]/span').click()

