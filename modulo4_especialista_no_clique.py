# Como usar a função clique
import pyautogui

# click personalizado
pyautogui.click(x=1611,y=507,clicrs=1000,interval=0.1,button='left',duration=2)
#click na posição atual(com botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')
#clicar x vezes
pyautogui.click(clicks=10)
#funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()