import pytest
from ctreport_selenium.ctlistener import Test, Severity

from pages.accountsummarypage import AccountSummaryPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.onlinebankingpage import OnlineBankingPage


class Test_Validating_Links:
    test = None

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, driver):
        home = HomePage(driver)
        home.click_onlinebanking_link()

    @pytest.mark.parametrize("feature_name", ["Account Summary", "Account Activity", "Transfer Funds"])
    def test_validating_without_signin(self, driver, feature_name):
        self.test = Test("Validating Feature link With Out Signin" + feature_name)
        self.test.log("Navigated to Online Banking page")
        onlinebanking = OnlineBankingPage(driver)
        onlinebanking.click_feature_link(feature_name)
        self.test.verify_are_equal(driver.title, "Zero - Log in", "Verifying the title fo the page", Severity.MINOR)
        self.test.log("Navigated to the signin page")
        driver.back()

    @pytest.fixture(scope="class")
    def signin_setup(self, driver):
        home = HomePage(driver)
        home.click_signin_button()
        login = LoginPage(driver)
        login.do_login("username", "password")
        account = AccountSummaryPage(driver)
        account.click_title_link()
        home.click_onlinebanking_link()

    @pytest.mark.parametrize("feature_name", ["Account Summary", "Account Activity", "Transfer Funds"])
    def test_validating_with_signin(self, driver, signin_setup, feature_name):
        self.test = Test("Validating Feature link With Signin " + feature_name)
        self.test.log("Navigated to Online Banking page")
        onlinebanking = OnlineBankingPage(driver)
        onlinebanking.click_feature_link(feature_name)
        self.test.verify_are_equal(feature_name in driver.title, True, "Verifying the title fo the page- Is tile has "
                                                                       "the feature name", Severity.CRITICAL)
        self.test.log("Navigated to the feature page")
        driver.back()

    def teardown_method(self, method):
        Test_Validating_Links.test = self.test
