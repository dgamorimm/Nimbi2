from selenium import webdriver
from modelo.login import User
from modelo.requisicao import Requisicao
from processador.log import Logger
from openpyxl import load_workbook
from selenium.common.exceptions import NoSuchElementException
import os
import shutil
from time import sleep

logger = Logger().get()
logger.info('Teste - Automação NIMBI')

path_file = "c:\\Nimbi\\Requisição"
#logger.info('\n01 - Passou - Teste')

prefs = {"safebrowsing.enabled": True}
prefs2 = {"download.default_directory": path_file}

prefs.update(prefs2)

options = webdriver.ChromeOptions()
options.add_argument("-incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")
#options.add_argument("headless") - Ambos servem para rodar em background
#options.add_argument("disable-gpu")
#options.binary_location = "C:\\Users\\douglas.pinheiro\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"
options.add_experimental_option("prefs", prefs)
bot = webdriver.Chrome(options=options, port=5556)

bot.get("https://nimbi.com.br/portais/estacio/")

usuario = User(bot)

usuario.logar("EST1056883", "Ana@2018")

req = Requisicao(bot)

caminho = '../dados/RelatorioRequisicao.xlsx'
arquivo_excel = load_workbook(caminho)
planilha1 = arquivo_excel.active
qtd_line = planilha1.max_row

for i in range(2, qtd_line + 1):
    s_id_req = planilha1.cell(row=i, column=1).value
    s_status_req = planilha1.cell(row=i, column=3).value

    req.buscar_requisicao(s_id_req, s_status_req)
    sleep(2)
    try:
        bot.find_element_by_xpath("//div[@class='webb-req-search-fields-panel-label webb-cart-item-label webb-left x-component']")
    except NoSuchElementException as x:
        print(x)
        req.download_guia_anexos()
    else:
        req.download_guia_itens()

    dir_origem = 'C:/Nimbi/Requisição/'
    dir_destino = dir_origem + str(s_id_req)
    busca_arquivo = os.listdir(dir_origem)
    sleep(1)
    os.mkdir(dir_destino)
    if os.path.exists(dir_destino):
        shutil.rmtree(dir_destino,ignore_errors=True)
        sleep(1)
        os.mkdir(dir_destino)
    if os.path.exists("C:/Nimbi/Requisição/anexos.zip"):
        for aquivo in busca_arquivo:
            if aquivo.endswith('.zip'):
                shutil.move(os.path.join(dir_origem, aquivo), os.path.join(dir_destino, aquivo))
    else:
        print("Não existe anexo para a requisição {}".format(str(s_id_req)))
