from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
visibility_of_element_located
from time import sleep
from datetime import datetime

class User:
    def __init__(self, driver):
        self.driver = driver
        self.IN_LOGIN = (By.CSS_SELECTOR,"input[name='logon']")
        self.IN_SENHA = (By.CSS_SELECTOR,"input[name='password']")

        pass

    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def find_reduce(self, *locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def find_v(self, *locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))


    def frame_switch_id(self, id):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_id(id))

    def frame_switch_name(self, name):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_name(name))

    def validar_click(self,clique_certo = None):
        try:
            self.find(clique_certo).click()
        except Exception as x:
            print(x)
            sleep(5)
            return self.validar_click(clique_certo)

        """data_e_hora = datetime.now()
        data_e_hora_texto = data_e_hora.strftime('%d/%m/%Y %H:%M:%S')
        self.find(self.MEMO).send_keys("Saneamento realizado na data: {}".format(data_e_hora_texto))
        sleep(1)"""
    def logar(self,usu,pwd):
        self.find(self.IN_LOGIN).send_keys(usu)
        sleep(1)
        self.find(self.IN_SENHA).send_keys(pwd)
        sleep(1)
        self.find(self.IN_SENHA).send_keys(Keys.ENTER)
        sleep(5)
        pass
