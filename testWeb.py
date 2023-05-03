# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import unittest
# import time

# class TestFrontend(unittest.TestCase):
#     def setUp(self):
#         options = Options()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)
#         self.driver.get("http://127.0.0.1:5000")
    
#     def test_website_up(self):
#         print(self.driver.title)
#         self.assertEqual("Bookings", self.driver.title)

#     def test_formOne(self):
#         elements = ['fName','phoneN','room','dateS','age','numOfPpl','length']
#         for i in elements:
#             self.assertTrue(self.driver.find_element(By.NAME,i))

#     def test_formOneSubmit(self):
#         xpaths = [['/html/body/main/form/div/div[1]/div[1]/input',"selenium"],['/html/body/main/form/div/div[1]/div[2]/input','000 000 0000'],['/html/body/main/form/div/div[2]/div[1]/select','/html/body/main/form/div/div[2]/div[1]/select/option[1]'],['/html/body/main/form/div/div[2]/div[2]/input','18/5'],['/html/body/main/form/div/div[3]/div[1]/select','/html/body/main/form/div/div[3]/div[1]/select/option[1]'],['/html/body/main/form/div/div[3]/div[2]/input','10'],['/html/body/main/form/div/div[3]/div[3]/select','/html/body/main/form/div/div[3]/div[3]/select/option[1]']]
#         for i in xpaths:
#             self.driver.find_element(By.XPATH,i[0]).send_keys(i[1])
#         self.driver.find_element(By.XPATH,"/html/body/main/form/div/button").click()
#         self.assertEqual("Select Time", self.driver.title)

    
#     def test_formTwo(self):
#         xpaths = [['/html/body/main/form/div/div[1]/div[1]/input',"selenium"],['/html/body/main/form/div/div[1]/div[2]/input','000 000 0000'],['/html/body/main/form/div/div[2]/div[1]/select','/html/body/main/form/div/div[2]/div[1]/select/option[1]'],['/html/body/main/form/div/div[2]/div[2]/input','18/5'],['/html/body/main/form/div/div[3]/div[1]/select','/html/body/main/form/div/div[3]/div[1]/select/option[1]'],['/html/body/main/form/div/div[3]/div[2]/input','10'],['/html/body/main/form/div/div[3]/div[3]/select','/html/body/main/form/div/div[3]/div[3]/select/option[1]']]
#         for i in xpaths:
#             self.driver.find_element(By.XPATH,i[0]).send_keys(i[1])
#         self.driver.find_element(By.XPATH,"/html/body/main/form/div/button").click()
#         self.assertTrue( self.driver.find_element(By.NAME,"time"))

#     def test_inputsformTwo(self):
#         xpaths = [['/html/body/main/form/div/div[1]/div[1]/input',"selenium"],['/html/body/main/form/div/div[1]/div[2]/input','000 000 0000'],['/html/body/main/form/div/div[2]/div[1]/select','/html/body/main/form/div/div[2]/div[1]/select/option[1]'],['/html/body/main/form/div/div[2]/div[2]/input','18/5'],['/html/body/main/form/div/div[3]/div[1]/select','/html/body/main/form/div/div[3]/div[1]/select/option[1]'],['/html/body/main/form/div/div[3]/div[2]/input','10'],['/html/body/main/form/div/div[3]/div[3]/select','/html/body/main/form/div/div[3]/div[3]/select/option[1]']]
#         for i in xpaths:
#             self.driver.find_element(By.XPATH,i[0]).send_keys(i[1])
#         self.driver.find_element(By.XPATH,"/html/body/main/form/div/button").click()
        
#         self.driver.find_element(By.XPATH,"/html/body/main/form/div/div/select").send_keys('/html/body/main/form/div/div/select/option[0]')
#         self.driver.find_element(By.XPATH,"/html/body/main/form/div/button").click()
#         time.sleep(2)
#         self.assertEqual("Confirmation", self.driver.title)

#     def tearDown(self):
#         self.driver.close()
    

# #if __name__ == '__main__':
#    # unittest.main()


