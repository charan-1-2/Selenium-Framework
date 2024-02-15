from selenium.webdriver.common.by import By

class LoginPage:
    __username=(By.ID,'input-username')
    __password=(By.ID,'input-password')
    __go_button=(By.NAME,'login-button')

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,un):
        print('enter username:',un)
        self.driver.find_element(*self.__username).send_keys(un)

    def enter_password(self,pw):
        print('enter password:',pw)
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_go_button(self):
        print('click go button')
        self.driver.find_element(*self.__go_button).click()