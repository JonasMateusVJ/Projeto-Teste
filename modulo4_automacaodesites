import webbrowser
import pyautogui
from time import sleep
import pyperclip
 
#navegue até o site ...
webbrowser.open('https://cursoautomacao.netlify.app/?_gl=1*1eftlib*_ga*OTQ0OTYyNjkzLjE2OTcwNzk4ODA.*_ga_37GXT4VGQK*MTcxNzk3NjA1Ny4xMi4xLjE3MTc5NzYwNTcuMC4wLjA.')
#2 encontre o clique no campo "digite seu namo" dentro de Exemplos Alertas" e digite seu nome
pyautogui.moveTo(1587,136,duration=2)
pyautogui.scroll(-1000)

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.moveTo(1207,297,duration=1)
pyautogui.click(duration=1)
escrever_frase('Jonas Mateus')

#3 clicar em alerta, para gerar a lerta
pyautogui.moveTo(1228,334,duration=1)
pyautogui.click()
#4 feche a alerta
pyautogui.moveTo(977,156,duration=1)
pyautogui.click()
#5 suba a página totalmente para cima
pyautogui.scroll(1000)
pyautogui.scroll(-2000)
#6 desça apenas o suficiente para conseguir chegar até a secção que contem os arquivos para o qual você irá
#fazer o dowload deles (no caso você deve fazer essa parte também totalmente com pyautogui,
#nada de trabalho manual aqui) e clicar e movimentar o mouse da maneira que for necessário para baixar os
#os arquivos execel e pdf.
#execel
pyautogui.moveTo(338,378,duration=2)
pyautogui.click()
pyautogui.moveTo(1331,150,duration=2)
pyautogui.click()
pyautogui.moveTo(628,443,duration=2)
pyautogui.click()
#pdf
pyautogui.moveTo(508,382,duration=2)
pyautogui.click()
pyautogui.moveTo(1331,150,duration=2)
pyautogui.click()
pyautogui.moveTo(628,443,duration=2)
pyautogui.click()

#depois de ter feito isso, eu quero que vocÊ crie um alerta que diz "você terminou"
pyautogui.alert('Terminei')
#https://cursoautomacao.netlify.app/?_gl=1*1eftlib*_ga*OTQ0OTYyNjkzLjE2OTcwNzk4ODA.*_ga_37GXT4VGQK*MTcxNzk3NjA1Ny4xMi4xLjE3MTc5NzYwNTcuMC4wLjA.