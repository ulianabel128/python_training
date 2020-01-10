# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://translate.google.com/?hl=ru#view=home&op=translate&sl=auto&tl=ru&text=The%20new%20Selenium%20IDE%20is%20designed%20to%20record%20your%20interactions%20with%20websites%20to%20help%20you%20generate%20and%20maintain%20site%20automation%2C%20tests%2C%20and%20remove%20the%20need%20to%20manually%20step%20through%20repetitive%20takes.%20Features%20include%3A%0A%0A*%20Recording%20and%20playing%20back%20tests%20on%20Firefox%20and%20Chrome.%0A*%20Organizing%20tests%20into%20suites%20for%20easy%20management.%0A*%20Saving%20and%20loading%20scripts%2C%20for%20later%20playback.")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Документы'])[1]/following::div[10]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
