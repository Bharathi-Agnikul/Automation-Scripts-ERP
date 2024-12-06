from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


class FoodBeverages:

    def __init__(self, driver):
        self.driver = driver

    def icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='FoodEmployeeRole']//child::i"))
        ).click()

    def get_started(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Get_started"))
        ).click()

    def menudropdown(self):
        location_food = self.driver.find_element(By.ID, "location")
        dropdown = Select(location_food)
        self.select_from_dropdown(dropdown, ["IITM RP", "Shar", "Thaiyur"])

        # Beverages Dropdown
        menuclick = self.driver.find_element(By.ID, "dropdown-style")
        menuclick.click()
        beverages_click = self.driver.find_element(By.XPATH, "(//a[@id='fandbdropdown'])[2]")
        beverages_click.click()
        location_beverages = self.driver.find_element(By.ID, "location")
        dropdown1 = Select(location_beverages)
        self.select_from_dropdown(dropdown1, ["IITM RP", "Shar", "Thaiyur"])

    def request_food(self):
        self.select_food("Breakfast", "Breakfast_location")
        self.select_food("Lunch", "Lunch_location")
        self.select_food("Dinner", "Dinner_location")

        self.driver.execute_script("window.scrollBy(0, 200);")
        book_food = self.driver.find_element(By.XPATH, "//button[@onclick='submit_form()']")
        book_food.click()

    def booked_food(self):
        booked_food_menu = self.driver.find_element(By.XPATH, "(//a[@id = 'dropdown-style'])[3]")
        booked_food_menu.click()

        # Edit Breakfast Booking
        breakfast_edit = self.driver.find_element(By.XPATH, "//button[@data-target = '#BrakefastEdit']")
        breakfast_edit.click()

        # Confirm Booking at Other Place
        bookAtOtherPlace_yes = self.driver.find_element(By.XPATH, "//button[@id = 'yes_button']")
        bookAtOtherPlace_yes.click()

    def icon1(self):
        agnikul_icon = self.driver.find_element(By.XPATH, "//img[@id = 'image']")
        agnikul_icon.click()

    def select_from_dropdown(self, dropdown, options):
        for option in options:
            dropdown.select_by_visible_text(option)
            time.sleep(1)

    def select_food(self, food_type, location_id):
        food_toggle = self.driver.find_element(By.ID, food_type)
        food_toggle.click()
        location_food = self.driver.find_element(By.ID, location_id)
        dropdown = Select(location_food)
        self.select_from_dropdown(dropdown, ["Thaiyur", "Shar", "IITM RP"])