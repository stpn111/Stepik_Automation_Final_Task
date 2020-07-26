import pytest
import warnings
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class UnsupportedBrowserException(Exception):
    pass


# читаем параметры с консоли
def pytest_addoption(parser):
    parser.addoption('--url', default='http://stepik.org')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--language', default='en')


# делаем config браузера
@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    language = request.config.getoption('--language')

    return {'browser': browser, 'version': version, 'url': url, 'language': language}


@pytest.fixture(scope='function')
def browser(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    language = config['language']
    # чтобы не сыпало кучу ворнингов о закрытых сокетах
    warnings.filterwarnings(action="ignore", message="unclosed",
                            category=ResourceWarning)

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install(),
                                  options=options,
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )
    else:
        raise UnsupportedBrowserException(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    # даже с quit периодически почему-то не закрывается браузер, решается killall chromedriver
    driver.close()
    driver.quit()
