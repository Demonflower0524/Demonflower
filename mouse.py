import pyautogui
import time 

print(pyautogui.size()); #화면 사이즈
#pyautogui.mouseInfo();

# 474,50 361,51
pyautogui.moveTo(474,50, 2) # 좌표값으로 이동 / 2초 동안
pyautogui.dragTo(361,51, 2) # 위에서 이동한 좌표값에서 2초동안 좌표값으로 드래그

pyautogui.click(button='right') # 이동한 곳에서 오른쪽 클릭
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1)