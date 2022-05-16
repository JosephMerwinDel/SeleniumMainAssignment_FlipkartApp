import json
import pytest
import inspect
import logging

from Utils.driverfactory import DriverFactory

CONFIG_PATH = "/Users/jmerwin/PycharmProjects/SeleniumMainProject/config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = "https://www.flipkart.com/"

@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup(config):
    return config["base_url"] if "base_url" in config else DEFAULT_URL


@pytest.fixture()
def setup(request, config):
    global driver
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    if config["browser"] == "chrome":
        driver.maximize_window()
        request.cls.driver = driver
    yield
    driver.quit()


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
