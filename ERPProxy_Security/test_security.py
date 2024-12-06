import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from POM.POM_Security import Visitor_Management
from POM.POM_LoginPage import Login_Page
from conftest import setup
from selenium.webdriver.common.action_chains import ActionChains


class Test_Visitors:
    base_url = "http://localhost:3000/qr_code/"
    username = "Administrator"
    password = "Agnikul_1"

    def test_security1(self, setup):  # Pass the setup fixture as a parameter
        self.driver = setup  # Use the WebDriver instance provided by the fixture
        self.driver.get(self.base_url)

        # Locate the username input field and send the username
        self.driver.find_element(By.XPATH, "//input[@id=':r0:']").send_keys(self.username)
        time.sleep(2)

        # Optionally, verify if the username was entered correctly
        username_value = self.driver.find_element(By.XPATH, "//input[@id=':r0:']").get_attribute("value")
        assert username_value == self.username, "The username was not entered correctly."

        self.driver.find_element(By.XPATH, "//input[@id=':r1:']").send_keys(self.password)
        time.sleep(2)

        # Optionally, verify if the username was entered correctly
        password_value = self.driver.find_element(By.XPATH, "//input[@id=':r1:']").get_attribute("value")
        assert password_value == self.password, "The password was not entered correctly."
        time.sleep(2)

        login_click = self.driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
        login_click.click()

        visitor_management = Visitor_Management(self.driver)
        visitor_management.entry()
        visitor_management.entry_laptop()
        visitor_management.entry_mobile()
        visitor_management.entry_confiscated_items()
        visitor_management.exit_t()
        visitor_management.exit_laptop()
        visitor_management.exit_confiscatedItems()
        visitor_management.logout()
