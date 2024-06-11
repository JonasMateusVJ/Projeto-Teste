import webbrowser
import pyautogui
from time import sleep
webbrowser.open('')
sleep(1)
#clicar dentro do site
pyautogui.click(10,10,duration=1)
#scroll até o ponto desejado
pyautogui.scroll(-1000)
sleep(1)
#encontrar e clicar no campo "digite seu nome"
campo_digite_seu_nome = pyautogui.locateOnScreen
('digite_seu_nome')
pyautogui.click(campo_digite_seu_nome[0],campo_digite_seu_nome[1],duration=1)
#digitar meu nome
pyautogui.typewrite('jonas mateus')
#abrir alerta
botao_alerta = pyautogui.locateCenterOnScreen('alerta.png')
pyautogui.click(botao_alerta[0],botao_alerta[1],duration=1)
sleep(1)
#fechar alerta
botao_ok = pyautogui.locateAllOnScreen('ok.png')
pyautogui.click(botao_ok[0],botao_ok[1],duration=1)
sleep(1)
#subir toda pagina
pyautogui.scroll(1000)
sleep(1)
pyautogui.scroll(-2000)
sleep(1)
#baixar arquivo execel
texto_execel = pyautogui.locateCenterOnScreen('execel.png')
pyautogui.moveTo(0,40,duration=1)
pyautogui.click()
sleep(1)
#clicar em algum ponto para sair da janela de download
pyautogui.click(1504,38,duration=1)
sleep(1)
#baixar pdf
arquivo_pdf = pyautogui.locateCenterOnScreen('arquivo_pdf.png')
pyautogui.moveTo(0,40,duration=1)
pyautogui.click()
#alerta
pyautogui.alert('Terminei')



