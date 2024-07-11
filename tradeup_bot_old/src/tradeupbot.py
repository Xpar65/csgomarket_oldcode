import pyautogui
import time
import os

def mouse_loc():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')
        return

def csgo_launch():
    #os.startfile("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\game\\bin\\win64\\cs2.exe")
    #https://pyautogui.readthedocs.io/en/latest/screenshot.html
    #wait about 30sec or make funciton looking for end of loading screen 
    time.sleep(20)
    #goto inven
    pyautogui.click(x=730, y=30)
    time.sleep(0.1)
        #check for new item prompt
    #goto tradeup
    pyautogui.click(x=1187, y=88)
    time.sleep(0.1)
    #goto quality drop down
    pyautogui.click(x=712, y=205)
    pyautogui.click(x=712, y=205)
    time.sleep(0.1)
    #goto newest
    pyautogui.click(x=727, y=252)
    time.sleep(0.1)
    #include checks to see if we are in correct state
    return
    
os.startfile("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\game\\bin\\win64\\cs2.exe")
#this closes when the script is stopped running. 
csgo_launch()

    
mouse_loc()
