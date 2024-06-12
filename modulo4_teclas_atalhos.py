import pyautogui
from time import sleep

#COMANDO PARA IMPRIMIR CÓDIGO DO TECLADO print (pyautogui.KEYBOARD_KEYS)
#deslocar para local que quer copiar
pyautogui.moveTo(10,10,duration=2)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
#deslocar para área a copiar
pyautogui.moveTo(10,10,duration=2)
pyautogui.hotkey('ctrl','v')

pyautogui.click(10,19,duration=2)
sleep(1)
#digitar algo
pyautogui.typewrite('digitando algo')
sleep(1)
#simula tecla tab
pyautogui.press('tab')
#simula tecla de espaço
pyautogui.press('space')