import time
from ast import Index

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from urllib3 import request
from selenium.webdriver.common.action_chains import ActionChains


class Visitor_Management:
    def __init__(self, driver):
        self.driver = driver

    def entry(self):
        time.sleep(2)
        entryIcon = self.driver.find_element(By.XPATH, "//div[@class='Entry-WelcomePage']")
        entryIcon.click()
        time.sleep(10)

    def entry_laptop(self):
        action = ActionChains(self.driver)
        action.scroll_by_amount(0, 500).perform()
        time.sleep(2)
        laptop_access = self.driver.find_element(By.XPATH, "(//input[@name=':r0:'])[2]")
        laptop_access.click()
        time.sleep(2)

    def entry_mobile(self):
        time.sleep(1)
        mobile_access = self.driver.find_element(By.XPATH, "(//input[@name=':r1:'])[1]")
        mobile_access.click()
        time.sleep(2)
        mobile_count = self.driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
        action = ActionChains(self.driver)
        action.scroll_by_amount(0, 500).perform()
        for hi in range(3):  # Adjust the range for the number of clicks needed
            mobile_count.click()
            time.sleep(1)
        slot_num = self.driver.find_element(By.XPATH, "//input[@inputmode='numeric']")
        slot_num.send_keys("123")
        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        next_button.click()
        time.sleep(2)

    def entry_confiscated_items(self):
        pendrive = self.driver.find_element(By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-4 "
                                           "MuiGrid-grid-md-3 css-pq7chb']//child::input[@name='pendrive']")

        pendrive.click()
        time.sleep(2)
        capture_button = self.driver.find_element(By.XPATH, "//button[@class='webcam-btnNew']")
        capture_button.click()
        time.sleep(2)
        #Entry
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(5)

    def exit_t(self):
        time.sleep(2)
        exitIcon = self.driver.find_element(By.XPATH, "//div[@class='Exit-WelcomePage']")
        exitIcon.click()
        time.sleep(10)

    def exit_laptop(self):
        time.sleep(2)
        action = ActionChains(self.driver)
        action.scroll_by_amount(0, 500).perform()
        time.sleep(2)
        laptop_access = self.driver.find_element(By.XPATH, "(//input[@name=':r0:'])[2]")
        laptop_access.click()
        mobile_return = self.driver.find_element(By.XPATH, "(//label[@class = 'MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd css-1jaw3da'])[3]")
        mobile_return.click()
        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        next_button.click()
        time.sleep(2)

        #Exiting
    def exit_confiscatedItems(self):
        exit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        exit_button.click()
        time.sleep(5)

    def logout(self):
        logoutbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        logoutbutton.click()
        time.sleep(5)