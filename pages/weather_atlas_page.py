from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage


class WeatherAtlasPage(BasePage):

    url = 'https://www.weather-atlas.com/'

    @property
    def save_preferences(self):
        locator = Locator(By.XPATH, '//button[text()="Save my preferences"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def today_date(self):
        locator = Locator(By.CSS_SELECTOR, 'h2[id="today"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def temperature_web_day(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="text-danger font_175_rem"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def temperature_web_night(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="text-primary font_150_rem"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def fahrenheit_button(self):
        locator = Locator(By.XPATH, '(//a[text()="°Fahrenheit"])[2]')
        return BaseElement(driver=self.driver, locator=locator)