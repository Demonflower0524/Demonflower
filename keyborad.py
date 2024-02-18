import pyautogui
import pyperclip

#pyautogui.moveTo(748,176, 2)
#pyautogui.click()
#pyautogui.write('tprtm', interval=0.1)

pyautogui.moveTo(373,100,1)
pyautogui.click()
pyautogui.dragTo(1853,708,1)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('delete')
pyautogui.hotkey('ctrl', 'v')