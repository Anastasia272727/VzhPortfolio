from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import random
import time
import unittest
from unittest import TestCase as TC

class TestAutoExercise(TC):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        fake = Faker(["ru_RU"])
        self.name = fake.name()
        self.phone_number = fake.phone_number()
        self.email = "1234@mail.ru"
        self.message = fake.text()
        self.password = "123456"
        self.text1 = 'Спасибо за заказ!'
        self.text2 = "Name on Card"
        self.text3 = "1234567887654321"
        self.text4 = "123"
        self.text5 = "12"
        self.text6 = "2025"
        self.URL = "https://automationexercise.com"
        self.browser.get(self.URL)

    def tearDown(self):
        self.browser.quit()

    def test_Autoexercise(self):
        element = self.browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")
        element.click()
        element = self.browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
        element.send_keys(self.email)
        element = self.browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
        element.send_keys(self.password)
        element = self.browser.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/button")
        element.click()
        element = self.browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/div[5]/div/div[2]/ul/li/a')
        self.browser.execute_script("arguments[0].click();", element)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')
        element.click()
        element = self.browser.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div[1]/div/div/div[3]/button')
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = self.browser.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div[1]/div/div/div[3]/button')
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div/div[1]/div/div[1]/div[2]/div[1]/h4/a')
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div/div[1]/div/div[1]/div[2]/div[2]/div/ul/li[2]/a')
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = self.browser.find_element(By.XPATH, "/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li/a")
        element.click()
        time.sleep(1)
        element = self.browser.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')
        element.click()
        time.sleep(1)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]/a')
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(3)
        element = self.browser.find_element(By.XPATH,'/html/body/section/div/section/div[1]/div/div/a')
        element.click()
        element = self.browser.find_element(By.XPATH,'/html/body/section/div/div[6]/textarea')
        element.send_keys(self.text1)
        time.sleep(3)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div[7]/a')
        element.click()
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div[3]/div/div[2]/form/div[1]/div/input')
        element.send_keys(self.text2)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div[3]/div/div[2]/form/div[2]/div/input')
        element.send_keys(self.text3)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[1]/input')
        element.send_keys(self.text4)
        element = self.browser.find_element(By.XPATH, '/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[2]/input')
        element.send_keys(self.text5)
        element = self.browser.find_element(By.XPATH,'/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[3]/input')
        element.send_keys(self.text6)
        element = self.browser.find_element(By.XPATH,'/html/body/section/div/div[3]/div/div[2]/form/div[5]/div/button')
        element.click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()






        # element = self.browser.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[1]/div/div/div[3]/button')
        # self.browser.execute_script("arguments[0].click();", element)
        # time.sleep(2)



        # element = self.browser.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[2]/div[2]/div/div[1]/div/a')
        # element.click()
        # self.browser.execute_script("window.scrollBy(0, 250)")
        # element = self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div[3]/div[2]/div/form/div[2]/ul/li[4]/label/span")
        # element.click()














# element = self.browser.find_element(By.XPATH,'/html/body/div[1]/header/div[4]/div/div/div[2]/div/a[1]/span')
# self.browser.execute_script("arguments[0].click();", element)