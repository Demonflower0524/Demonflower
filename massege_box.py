import pyautogui as pg

#a = pg.alert(text='버튼을 눌러주세요.', title='알림', button='OK')
#a = pg.confirm(text='버튼을 눌러주세요.', title='알림', buttons=['ok', 'cancel'])
#print(a)

#b = pg.prompt(text='버튼을 눌러주세요.', title='알림', default='문자를 입력해주세요.')
#print(b)

c = pg.password(text='버튼을 눌러주세요.', title='알림', mask='*')
print(c)