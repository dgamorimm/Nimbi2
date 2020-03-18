from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
visibility_of_element_located, presence_of_element_located_s
from time import sleep
import os


class Requisicao:
    def __init__(self, driver):
        self.driver = driver
        # Selecionar a aba de requisição
        self.CLICK_REQ = (By.ID,"requisition-tab")
        # Inclusão do ID
        self.IN_REQ_ID = (By.NAME,"REQUISITION_WEBB_ID_NAME")#"x-auto-1553-input")
        # Selecionar o status
        self.CLICK_STATUS = (By.NAME,"REQUISITION_STATUS_NAME" )#"x-auto-1555-input")
        self.LISTA_STATUS = (By.CLASS_NAME,"x-combo-list-item ")
        # limpar criação de data
        self.IN_DATAINIT = (By.ID, "start-date-input")
        # buscar
        self.ENTER_BUSCAR = (By.ID,"end-date-input")
        # entrando pelo icone de folder
        self.CLICK_ENTRAR = (By.NAME,"REQUISITION_OPEN_IMAGE_0_10_NAME")
        # clicando no icone de anexo
        self.ANEXOS = (By.CLASS_NAME,"x-grid3-col-ATTACHMENT_CLIP")
        # fazendo o download
        # funciona self.ENTER_BAIXAR = (By.CSS_SELECTOR,"td:nth-child(1) > div > table > tbody > tr:nth-child(1) > td > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td.x-btn-mc > em > button[type='button']")#"x-window-body")#(By.ID,"x-auto-6061")
        self.ENTER_BAIXAR = (By.XPATH,"//*[@class=' x-btn webb-icon-button4 x-component  x-btn-text-icon x-item-disabled x-unselectable']/tbody/tr[2]/td[2]/em/button")
        self.VALIDAR_ANEXO = (By.CSS_SELECTOR, "td > div > div.x-panel-bwrap > div.x-panel-body.x-panel-body-noheader.x-form-label-left > div:nth-child(2) > div.x-edit-grid.x-grid-panel.x-component.x-border > div.x-grid3 > div.x-grid3-viewport > div.x-grid3-scroller > div > div")
        self.FECHAR_ANEXO = (By.CSS_SELECTOR,"div.x-window-tl > div > div > div > div > table > tbody > tr > td > div")

        self.GUIA_ANEXO = (By.CLASS_NAME,"x-panel-header-text")
        self.ANEXOS_SEC = (By.XPATH,"//div[@class='webb-req-search-fields-panel-label webb-cart-item-label webb-left x-component']")
        self.CLICK_INICIO = (By.ID,"home-tab")

        ############################################################################################

        pass

    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def finds(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located_s(*locator))

    def find_reduce(self, *locator, timeout=3):
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

    def validar_click_reduce(self,clique_certo = None):
        try:
            self.find_reduce(clique_certo).click()
        except IOError as x:
            print(x)
            sleep(5)
            return self.validar_click_reduce(clique_certo)

    def validar_click_imediato(self,clique_certo = None):
        try:
            clique_certo.click()
        except IOError as x:
            print(x)
            sleep(5)
            return self.validar_click_imediato(clique_certo)


    def buscar_requisicao(self,id,status):
        driver = self.driver
        self.frame_switch_name("topMenu")

        self.validar_click(self.CLICK_REQ)
        sleep(3)

        driver.switch_to.parent_frame()
        self.frame_switch_name("gwtIndex")

        self.validar_click(self.IN_REQ_ID)
        self.find(self.IN_REQ_ID).clear()
        self.find(self.IN_REQ_ID).send_keys(id)
        sleep(1)

        self.validar_click(self.CLICK_STATUS)
        sleep(1)

        lista_sts = self.finds(self.LISTA_STATUS)

        try:
            for self.valor in lista_sts:
                if self.valor.text == status:
                    self.valor.click()
                    break
        except:
            return exit()

        self.validar_click(self.IN_REQ_ID)
        sleep(1)
        self.find(self.IN_REQ_ID).send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + "Todos")
        sleep(1)
        self.find(self.IN_DATAINIT).clear()
        sleep(1)
        self.find(self.ENTER_BUSCAR).clear()
        sleep(1)
        self.validar_click(self.ENTER_BUSCAR)
        self.find(self.ENTER_BUSCAR).send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
        sleep(2)

        self.validar_click(self.CLICK_ENTRAR)
        sleep(2)
        pass

    def download_guia_anexos(self):
        #anexo na guia de anexo
        try:
            botao = self.finds(self.ENTER_BAIXAR)
            self.validar_click_imediato(botao[1])
            sleep(2)
            botao[1].send_keys(Keys.TAB + Keys.ENTER)
            sleep(1)
            while True:
                if os.path.exists('C:/Nimbi/Downloads/anexos (1).zip') or os.path.exists('C:/Nimbi/Downloads/anexos.zip'):
                    sleep(1)
                    sleep(3)
                    break
        except NoSuchElementException as x:
            print(x)
            sleep(3)


    def download_guia_itens(self):
        sleep(2)
        botao = self.finds(self.ENTER_BAIXAR)
        try:
            self.validar_click_imediato(botao[5])
            botao[5].send_keys(Keys.TAB + Keys.ENTER)
            sleep(1)
            while True:
                if os.path.exists('C:/Nimbi/Downloads/anexos.zip'):
                    sleep(1)
                    self.validar_click_reduce(self.FECHAR_ANEXO)
                    sleep(3)
                    break
        except:
            self.validar_click_imediato(botao[3])
            botao[3].send_keys(Keys.TAB + Keys.ENTER)
            sleep(1)
            while True:
                if os.path.exists('C:/Nimbi/Downloads/anexos.zip'):
                    sleep(1)
                    self.validar_click_reduce(self.FECHAR_ANEXO)
                    sleep(3)
                    break

