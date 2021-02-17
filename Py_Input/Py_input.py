import time
import pyautogui
print('\n종료하려면 Ctrl-C를 누르십시요!')
cnt = 0;
try:
    while True:
        cnt += 1
        pyautogui.typewrite('H', interval=2)
        print('\n{}회 마우스 움직임을 제어 하였습니다.'.format(cnt))
        time.sleep(10)
except KeyboardInterrupt:
    print('\n작업이 종료 되였습니다.')