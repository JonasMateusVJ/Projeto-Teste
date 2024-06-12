import pyautogui
#localiza a imagem pelas coordenadas do arquivo de imagem gravado
captcha = pyautogui.locateCenterOnScreen('google.png')
#clica na imagem
pyautogui.click(captcha[0],captcha[1],duration=2)

#https://www.google.com/recaptcha/api2/demo?_gl=1*dpg2d1*_ga*OTQ0OTYyNjkzLjE2OTcwNzk4ODA.*_ga_37GXT4VGQK*MTcxNzk3MTAzNC4xMS4xLjE3MTc5NzIyMTAuMC4wLjA.