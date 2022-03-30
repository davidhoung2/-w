import random
import time, os
# from PIL import Image
# import pytesseract as pytesseract
import cv2
import mss
import numpy
import win32api

import auto_player as player

# pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


# pyautogui.screenshot()

def auto_play_w_multi():
    dist = 0
    while True:
        if player.find_touch_multi('fight_1360x765', monitor, dist, n, tap=False):
            im = numpy.array(mss.mss().grab(monitor))
            screen = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
            wanted = player.imgs['fight_1360x765']
            dist = player.locate(screen, wanted)
            dist = numpy.array(dist)  # [[x,y]]
            dist = dist[0]  # [x,y]
            dist = dist[0]  # 找出圖片的x座標
            print(dist)
            '''t = random.uniform(0.5, 1.5)
            time.sleep(t)
            xx = player.random_offset(tele_pos, 5, 5)
            player.touch(xx)'''
            player.find_touch_multi('teleport_960x540', monitor, dist, n, tap=True)
            '''
            player.random_delay()
            xx = player.random_offset(setting_pos, 2, 2)
            player.touch(xx)
            '''
            player.find_touch_multi('setting_960x540', monitor, dist, n, tap=True)
            player.find_touch_multi('mode_960x540', monitor, dist, n, tap=True)
            '''t = random.uniform(1.5, 2)
            time.sleep(t)
            xx = player.random_offset(mode_pos, 100, 100)
            player.touch(xx)'''

        elif player.find_touch('no_response', monitor, tap=False):
            player.find_touch_multi('no_response', monitor, tap=True)

        elif player.find_touch_multi('terminate', monitor, dist, n, tap=False) or player.find_touch_multi('x', monitor, dist, n, tap=True):
            break

        elif player.find_touch_multi('terminate1', monitor, dist, n, tap=False) or player.find_touch_multi('x', monitor, dist, n, tap=True):
            break

        elif player.find_touch('control', monitor, tap=False):
            if player.find_touch('assist', monitor, tap=False):
                player.find_touch('assist', monitor, tap=True)
                player.find_touch('setting_960x540', monitor, tap=True)
                player.find_touch('mode_960x540', monitor, tap=True)
            elif player.find_touch('assisting', monitor, tap=False):
                player.find_touch('setting_960x540', monitor, tap=True)
                player.find_touch('mode_960x540', monitor, tap=True)
            elif player.find_touch('assisting_1', monitor, tap=False):
                player.find_touch('setting_960x540', monitor, tap=True)
                player.find_touch('mode_960x540', monitor, tap=True)
            elif player.find_touch('assisting_2', monitor, tap=False):
                player.find_touch('setting_960x540', monitor, tap=True)
                player.find_touch('mode_960x540', monitor, tap=True)


        t = random.uniform(1, 3)
        time.sleep(t)


def auto_play_w():
    tele_pos = [1804, 715]
    setting_pos = [551, 511]
    mode_pos = [1196, 433]
    print('每3秒偵測一次\n')
    im = numpy.array(mss.mss().grab(monitor))
    screen = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
    wanted = player.imgs['fight_1360x765']
    dist = player.locate(screen, wanted)
    dist = numpy.array(dist)
    while True:

        if player.find_touch('fight_1360x765', monitor, tap=False):
            '''t = random.uniform(0.5, 1.5)
            time.sleep(t)
            xx = player.random_offset(tele_pos, 5, 5)
            player.touch(xx)'''
            player.find_touch('teleport_1360x765', monitor, tap=True)
            '''
            player.random_delay()
            xx = player.random_offset(setting_pos, 2, 2)
            player.touch(xx)
            '''
            player.find_touch('setting_1360x765', monitor, tap=True)
            player.find_touch('mode_1360x765', monitor, tap=True)
            '''t = random.uniform(1.5, 2)
            time.sleep(t)
            xx = player.random_offset(mode_pos, 100, 100)
            player.touch(xx)'''
        t = random.uniform(1, 2)
        time.sleep(t)


def terminate():
    player.find_touch('w', monitor, tap=True)
    player.find_touch('w_1', monitor, tap=True)
    player.find_touch('start', monitor, tap=True)
    player.find_touch('start1', monitor, tap=True)
    player.find_touch('start_game', monitor, tap=True)
    if player.find_touch('assist', monitor, tap=True):
        player.find_touch('setting_960x540', monitor, tap=True)
        player.find_touch('mode_960x540', monitor, tap=True)
        return auto_play_w_multi()
        time.sleep(3)


def menu(debug=False):
    menu_list = [
        [auto_play_w, '女兒工作囉 解析度:1360x765'],
        [auto_play_w_multi, '女兒工作囉 解析度:960x540 支援多開 (左右各1個) 以螢幕中間為分割點']
    ]
    i = 0
    for func, des in menu_list:
        msg = str(i) + ": " + des + '\n'
        print(msg)
        i += 1
    player.alarm(1)
    raw = input("選擇功能模式：")
    index = int(raw)
    func, des = menu_list[index]
    print('已選擇功能： ' + des + '\n')
    global n,h
    n = int(input('輸入螢幕寬度: '))
    h = int(input('輸入螢幕高度: '))
    upleft = (0, 0)
    downright = (n, h)
    a, b = upleft
    c, d = downright
    global monitor
    monitor = {"top": b, "left": a, "width": c, "height": d}
    while True:
        func()
        while True:
            terminate()


if __name__ == '__main__':
    '''while True:
        pt = win32api.GetCursorPos()
        print(pt)
        '''
    # pyinstaller -F autorun.py
    menu()
    # img = Image.open(r"wanted/blood.png")
    # print(pytesseract.image_to_string(img, lang="eng"))
