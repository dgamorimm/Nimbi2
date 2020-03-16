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
        # criado por todos
        #self.CLICK_CRIADOPOR = (By.TAG_NAME,"input[name='REQUISITION_CREATED_BY_NAME']")
        #self.BTN_CRIADOPOR_TODOS = (By.TAG_NAME,"label[name='0'][title='Todos']")
        # limpar criação de data
        self.IN_DATAINIT = (By.ID, "start-date-input")
        # buscar
        self.ENTER_BUSCAR = (By.ID,"end-date-input")
        # entrando pelo icone de folder
        self.CLICK_ENTRAR = (By.NAME,"REQUISITION_OPEN_IMAGE_0_10_NAME")
        # clicando no icone de anexo
        #self.ANEXOS = (By.TAG_NAME,"img[src='skin-webb/img/anexo_vazio.gif'][title='Anexos']")
        #self.ANEXOS = (By.XPATH,"//img[@src='skin-webb/img/anexo_vazio.gif'][@title='Anexos']")
        self.ANEXOS = (By.CLASS_NAME,"x-grid3-col-ATTACHMENT_CLIP")
        # fazendo o download
        self.ENTER_BAIXAR = (By.CSS_SELECTOR,"td:nth-child(1) > div > table > tbody > tr:nth-child(1) > td > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td.x-btn-mc > em > button[type='button']")#"x-window-body")#(By.ID,"x-auto-6061")
        self.VALIDAR_ANEXO = (By.CSS_SELECTOR, "td > div > div.x-panel-bwrap > div.x-panel-body.x-panel-body-noheader.x-form-label-left > div:nth-child(2) > div.x-edit-grid.x-grid-panel.x-component.x-border > div.x-grid3 > div.x-grid3-viewport > div.x-grid3-scroller > div > div")
        self.FECHAR_ANEXO = (By.CSS_SELECTOR,"div.x-window-tl > div > div > div > div > table > tbody > tr > td > div")

        self.GUIA_ANEXO = (By.CLASS_NAME,"x-panel-header-text")
        self.ANEXOS_SEC = (By.XPATH,"//div[@class='webb-req-search-fields-panel-label webb-cart-item-label webb-left x-component']")
        self.CLICK_INICIO = (By.ID,"home-tab")

        "#x-auto-16291 > tbody > tr:nth-child(2) > td.x-btn-mc > em"
        "#x-auto-16735 > tbody > tr:nth-child(2) > td.x-btn-mc > em > button"

        "#x-auto-16734 > tbody > tr:nth-child(2) > td.x-btn-ml"
        "#x-auto-16745"
        # x-auto-16736 > table > tbody > tr > td:nth-child(3)
        "#x-auto-16736 > table > tbody > tr > td:nth-child(2)"
        "div#requisition-tab"
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
        driver = self.driver
        try:
            self.validar_click_reduce(self.ENTER_BAIXAR)
            sleep(2)
            self.find_reduce(self.ENTER_BAIXAR).send_keys(Keys.TAB + Keys.ENTER)
            sleep(1)
            while True:
                if os.path.exists("C:/Nimbi/Requisição/anexos.zip"):
                    sleep(1)
                    driver.refresh()
                    sleep(3)
                    break
        except NoSuchElementException as x:
            print(x)
            driver.refresh()
            sleep(3)


    def download_guia_itens(self):
        sleep(3)
        driver = self.driver
        # anexo na guia de item
        anexs = self.finds(self.ANEXOS)
        for self.anex in anexs:
            id_anexo_texto = self.anex.text
            if id_anexo_texto != "":
                self.anex.click()
                sleep(1)
                anexo = self.find(self.VALIDAR_ANEXO)
                if anexo.text != " ":
                    self.validar_click(self.ENTER_BAIXAR)
                    sleep(2)
                    try:
                        self.find(self.ENTER_BAIXAR).send_keys(Keys.TAB + Keys.ENTER)
                        sleep(1)
                        while True:
                            if os.path.exists("C:/Nimbi/Requisição/anexos.zip"):
                                sleep(1)
                                self.validar_click_reduce(self.FECHAR_ANEXO)
                                sleep(3)
                                break
                    except:
                        driver.refresh()
                        return sleep(3)
                else:
                    driver.refresh()
                    sleep(3)
        driver.refresh()
        sleep(3)

