from pages.basepage import BasePage
from selenium.webdriver.common.by import By
import time

class AccountSummaryPage(BasePage):
    pay_bills_link = By.XPATH, "//a[text()='Pay Bills']"
    title_link = By.XPATH, "//a[text()='Zero Bank']"

    def click_pay_bills_link(self):
        time.sleep(5)
        self._click(self.pay_bills_link)

    def click_title_link(self):
        self._click(self.title_link)