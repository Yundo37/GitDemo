import pytest

from selenium import webdriver
driver = None
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver as EdgeDriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    #if browser_name == "chrome":
        #service_obj = ChromeService("C:/Users/YB/Documents/chromedriver/chromedriver.exe")
        #driver = webdriver.Chrome(service=service_obj) ✅ 수동 방식 제거
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        driver = webdriver.Chrome(options=options)  # ✅ 자동 드라이버 관리 (Selenium 4.34.2)

    elif browser_name == "edge":
        service_obj = EdgeService("C:/Users/YB/Documents/edgedriver/msedgedriver.exe")
        driver = EdgeDriver(service=service_obj)



    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)