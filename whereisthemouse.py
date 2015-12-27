'''THIS IS NOT MY CODE. I got it from the pyautogui documentation. It was pretty useful for finding where the mouse should be'''


import pyautogui, sys
import time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print('\n')
