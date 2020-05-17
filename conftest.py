from pathlib import Path

import pytest
from selenium import webdriver

from _pytest.runner import runtestprotocol
from ctreport_selenium.ctlistener import Session

from pages.homepage import HomePage
from pages.loginpage import LoginPage


@pytest.fixture(scope="session",autouse=True)
def driver(request):
    driver_ = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")

    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com")

    session_details = {
        "owner": "Naveen.S",
        "application": "Zero Bank",
        "application version": "V1.04",
        "os": "Windows10",
        "browser": "Chrome 83"
    }
    report_options = {
        "title": "Test Report",
        "logo": r"D:\MYLOGO.PNG",
        "show_reference": True,
    }
    Session.start(test_name="Smoke Test - MyApp1",
                  path=str(Path(__file__).parent)+r"\reports",
                  driver=driver_,
                  session_details=session_details,
                  report_options=report_options)

    def quit():
        driver_.quit()
        Session.end()

    request.addfinalizer(quit)
    return driver_



def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when== 'setup':
            test = item.cls.test
        if report.when == 'call':
            if report.outcome == 'skipped':
                test.skip(report.longrepr[2])
            if report.outcome == 'failed':
                test.broken(report.longrepr.reprcrash.message)
        if report.when == 'teardown':
            test.finish()
    return False

def pytest_sessionfinish(session):
    Session.end()
