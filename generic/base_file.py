import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class BaseTest:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        print('Reading config.properties')
        p = Properties()
        p.load(open('../config.properties'))
        grid=p['GRID']
        grid_url=p['GRID_URL']
        browser=p['BROWSER']
        app_url=p['APP_URL']
        ito=p['ITO']
        eto=p['ETO']

        if grid.lower()=='yes':
            print('Using Grid')
            if browser.lower()=='firefox':
                print('Open the Firefox Browser')
                options=FirefoxOptions()
            else:
                print('Open the Chrome Browser')
                options = ChromeOptions()

            self.driver = Remote(command_executor=grid_url, options=options)
        else:
            print('Using Local System')
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