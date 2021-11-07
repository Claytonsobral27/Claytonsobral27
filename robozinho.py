import pyautogui
import time

import pymsgbox 

pyautogui.PAUSE = 3.5

pyautogui.press('win')
pyautogui.write('visual code')
pyautogui.press('enter')

pyautogui.click(x=95, y=15)
#clica no aquivo
pyautogui.click(x=144, y=243)
#clica abrir pasta
pyautogui.click(x=126, y=302)
#clica em documentos
pyautogui.click(x=354, y=249)
#selecionar pasta
pyautogui.click(y=686, x=672)
#mover para aparecer o incone de arquivos


pyautogui.click(y=325, x=116)
pyautogui.click(y=325, x=116)


pyautogui.write('index.html')
pyautogui.write('!')
pyautogui.press('enter')



