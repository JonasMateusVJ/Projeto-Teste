import pyautogui

for i in range(5):
    #mover  até uma coordenada
    pyautogui.moveTo(1106,180,duration=1.5)
    #clicar arrastar até um ponto e soltar
    pyautogui.dragTo(1116,580,button='left',duration=1.5)
    #repetir 5 vezes