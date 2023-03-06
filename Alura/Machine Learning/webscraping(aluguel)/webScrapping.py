
from pyautogui import *
from time import sleep
# sleep(1)

hotkey('alt','tab')
# https://1xbet.whoscored.com/Regions/31/Tournaments/95/Seasons/8984/Stages/20566/PlayerStatistics/Brazil-Brasileir%C3%A3o-2022

sleep(1)

keyDown('alt')
press('tab')
sleep(.5)
press('tab')
keyUp('alt')
sleep(1)

for i in range(66):
    tempo = 0.1
    click(x=1218, y=691)

    dragTo(x=166, y=275)
    sleep(tempo)
    hotkey('ctrl','c')
    sleep(tempo)


    keyDown('alt')
    press('tab')
    sleep(tempo)

    # press('tab')
    keyUp('alt')
    sleep(tempo)
    hotkey('ctrl','v')
    sleep(tempo)

    click(x=921, y=496) # clica no OK do excel
    sleep(tempo)
    sleep(tempo)
    press('pgdn')
    sleep(tempo)
    hotkey('alt','tab')
    sleep(tempo)
    click(x=1186, y=735)
    sleep(1.5)
hotkey('alt','tab')
hotkey('ctrl','n')
hotkey('alt','tab')
hotkey('ctrl','s')

