import pyautogui, keyboard
def restart():
    while True:
        if keyboard.is_pressed('1'):
            start()
def start():
    while keyboard.is_pressed('2') == False:
        pyautogui.click()
    else:
        restart()
restart()
