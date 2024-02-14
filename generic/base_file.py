import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties

class BaseTest:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        print('Reading config.properties')
        p = Properties()
        p.load(open('../config.properties'))
        browser=p['BROWSER']
        app_url=p['APP_URL']
        ito=p['ITO']
        eto=p['ETO']

        if browser.lower()=='firefox':
            print('Open the Firefox Browser')
            self.driver=Firefox()
        else:
            print('Open the Chrome Browser')
            self.driver=Chrome()

        print('Enter the url',app_url)
        self.driver.get(app_url)
        print('Set ITO:',ito)
        self.driver.implicitly_wait(ito)
        print('Set ETO:',eto)
        self.wait=WebDriverWait(self.driver,eto)
        print('Maximize the browser')
        self.driver.maximize_window()

    @pytest.fixture(autouse=True)
    def post_condtion(self):
        yield
        print('Close the browser')
        self.driver.close()