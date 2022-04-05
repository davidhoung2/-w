import datetime
import random
import time, os

from interval import Interval
import numpy as np
import pyautogui
from PIL import Image
import cv2
import mss
import numpy
import win32api
import win32con
import auto_player as player

def auto_play_w_multi():
    dist = 0
    select_move = 113
    while True:
        if player.find_touch('fight_1920x1080', monitor, tap=False):
            while not player.find_touch('teleport', monitor, tap=True):
                player.find_touch('teleport', monitor, tap=True)
                if player.find_touch('teleport', monitor, tap=True):
                    break
            while not player.find_touch('setting_1920x1080', monitor, tap=True):
                player.find_touch('setting_1920x1080', monitor, tap=True)
                if player.find_touch('setting_1920x1080', monitor, tap=True):
                    break
            while not player.find_touch('mode_1920x1080', monitor, tap=True):
                player.find_touch('mode_1920x1080', monitor, tap=True)
                if player.find_touch('mode_1920x1080', monitor, tap=True):
                    break


        # 如果偵測到沒有紅藥水
        elif player.find_touch('zero', monitor, tap=False):
            # 找看看是否存在其他數字
                win32api.keybd_event(27, 0, 0, 0)
                win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(1)
                while not player.find_touch_moveleft('home_map1', monitor, tap=True):
                    player.find_touch_moveleft('home_map1', monitor, tap=True)
                    if player.find_touch_moveleft('home_map1', monitor, tap=False):
                        break
                time.sleep(2)
                player.find_touch('teritory', monitor, tap=True)
                player.find_touch('home', monitor, tap=True)
                player.find_touch_unrand('home1', monitor, tap=True)
                player.find_touch('home_tp', monitor, tap=True)
                player.find_touch('correct', monitor, tap=True)
                time.sleep(10)
                player.find_touch('attack', monitor, tap=True)
                player.find_touch('shop', monitor, tap=True)
                if player.find_touch('shop_move', monitor, tap=True):
                    time.sleep(30)
                player.find_touch('buy', monitor, tap=True)
                player.find_touch('buy_all', monitor, tap=True)
                player.find_touch('exit', monitor, tap=True)
                if player.find_touch('lookup', monitor, tap=True) or player.find_touch('lookup1', monitor, tap=True):
                    if player.find_touch('prison', monitor, tap=True):
                        if m == 1:
                            player.find_touch('prison_1', monitor, tap=True)
                            if s == 1:
                                player.find_touch('move_prison', monitor, tap=True)
                                player.find_touch('correct', monitor, tap=True)
                            if s == 2:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                            if s == 3:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                        if m == 2:
                            player.find_touch('prison_2', monitor, tap=True)
                            if s == 1:
                                player.find_touch('move_prison', monitor, tap=True)
                                player.find_touch('correct', monitor, tap=True)
                            if s == 2:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                        if m == 3:
                            player.find_touch('prison_3', monitor, tap=True)
                            if s == 1:
                                player.find_touch('move_prison', monitor, tap=True)
                                player.find_touch('correct', monitor, tap=True)
                            if s == 2:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                            if s == 3:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                        if m == 4:
                            player.find_touch('prison_4', monitor, tap=True)
                            if s == 1:
                                player.find_touch('move_prison', monitor, tap=True)
                                player.find_touch('correct', monitor, tap=True)
                            if s == 2:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                            if s == 3:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                            #重第三層走入

                            '''
                            傳送到古魯丁3層
    
                            1.點小地圖
                            2.點到要的座標
                            3.按住D 2秒
                            4.偵測門
                            if 偵測不到門:
                                repeat 1~4 
                            '''
                            if s == 4:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 2)
                                    player.touch_p(go, y)# 傳到第三層
                                    time.sleep(1)
                                    player.find_touch('correct', monitor, tap=True)
                                    time.sleep(2)
                                    if player.find_touch('assisting', monitor, tap=True) or player.find_touch('assisting_2', monitor, tap=True):
                                        player.find_touch('assist', monitor, tap=True)

                                    player.find_touch('small_map_4', monitor, tap=True)
                                    time.sleep(2)
                                    #移動到位置
                                    player.find_touch('flag_4', monitor, tap=True)
                                    player.find_touch('move_4', monitor, tap=True)
                                    time.sleep(45)
                                    win32api.keybd_event(68, 0, 0, 0)
                                    time.sleep(2)
                                    win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                                    for i in range(5):
                                        if player.find_touch('transport_door_44', monitor, tap=True):
                                            break
                                        else:
                                            player.find_touch('small_map_4', monitor, tap=True)
                                            time.sleep(2)
                                            player.find_touch('flag_4', monitor, tap=True)
                                            player.find_touch('move_4', monitor, tap=True)
                                            time.sleep(10)
                                            win32api.keybd_event(68, 0, 0, 0)
                                            time.sleep(2)
                                            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                            '''if s == 5:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = player.random_simple(select_move * (s - 1))
                                    player.touch_p(go, y)
                                    player.find_touch('small_map_4', monitor, tap=True)
                            if s == 6:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = player.random_simple(select_move * (s - 1))
                                    player.touch_p(go, y)'''
                        if m == 5:
                            pt = win32api.GetCursorPos()
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(pt[0]), 0, 0, 0)
                            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                            time.sleep(2)
                            player.find_touch('prison_5', monitor, tap=True)

                            if s == 1:
                                player.find_touch('move_prison', monitor, tap=True)
                                player.find_touch('correct', monitor, tap=True)

                            if s == 2:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)

                            if s == 3:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)

                        if m == 6:
                            pt = win32api.GetCursorPos()
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(pt[0]), 0, 0, 0)
                            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                            time.sleep(2)
                            player.find_touch('prison_6', monitor, tap=True)

                            if s == 1:
                                player.find_touch('move_prison', monitor, tap=True)
                                player.find_touch('correct', monitor, tap=True)

                            if s == 2:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)

                            if s == 1.3:
                                ss = 3
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (ss - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)
                            if s == 4:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)

                            if s == 5:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)

                            if s == 6:
                                if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                    go = player.find_touch('move_prison', monitor, tap=False)
                                    y = select_move * (s - 1)
                                    player.touch_p(go, y)
                                    player.find_touch('correct', monitor, tap=True)

                            if s > 6 or s == 3:
                                pt = [int(1920/2), int(910)]
                                win32api.SetCursorPos(pt)
                                time.sleep(1)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, int((pt[0] - 1080) * 4), 0, 0)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, int((pt[0] - 1080) * 4), 0, 0)
                                time.sleep(2)
                                if s == 21:
                                    ss = 3
                                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                        go = player.find_touch('move_prison', monitor, tap=False)
                                        y = select_move * (ss - 1)
                                        player.touch_p(go, y)
                                        player.find_touch('correct', monitor, tap=True)

                                if s == 22:
                                    ss = 4
                                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                        go = player.find_touch('move_prison', monitor, tap=False)
                                        y = select_move * (ss - 1)
                                        player.touch_p(go, y)
                                        player.find_touch('correct', monitor, tap=True)

                                if s == 23:
                                    ss = 5
                                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                        go = player.find_touch('move_prison', monitor, tap=False)
                                        y = select_move * (ss - 1)
                                        player.touch_p(go, y)
                                        player.find_touch('correct', monitor, tap=True)

                                if s == 3:
                                    ss = 5
                                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                                        go = player.find_touch('move_prison', monitor, tap=False)
                                        y = select_move * (ss - 1)
                                        player.touch_p(go, y)  # 傳到第三層
                                        time.sleep(1)
                                        player.find_touch('correct', monitor, tap=True)
                                        time.sleep(2)
                                        if player.find_touch('assisting', monitor, tap=True) or player.find_touch(
                                                'assisting_2', monitor, tap=True):
                                            player.find_touch('assist', monitor, tap=True)

                                        player.find_touch('small_map_6', monitor, tap=True)
                                        time.sleep(2)
                                        # 移動到位置
                                        player.find_touch('flag_6', monitor, tap=True)
                                        player.find_touch('move_4', monitor, tap=True)
                                        time.sleep(30)
                                        win32api.keybd_event(65, 0, 0, 0)
                                        time.sleep(2)
                                        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
                                        for i in range(5):
                                            if player.find_touch('transport_door_44', monitor, tap=True):
                                                break
                                            else:
                                                player.find_touch('small_map_4', monitor, tap=True)
                                                time.sleep(2)
                                                player.find_touch('flag_6', monitor, tap=True)
                                                player.find_touch('move_4', monitor, tap=True)
                                                time.sleep(10)
                                                win32api.keybd_event(65, 0, 0, 0)
                                                time.sleep(2)
                                                win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)

        elif player.find_touch('no_response', monitor, tap=True):
            return terminate()

        elif player.find_touch('x', monitor, tap=True):
            return terminate()

        elif player.find_touch('terminate_1920x1080', monitor, tap=False):
            return terminate()

        elif player.find_touch('terminate1', monitor, tap=False):
            return terminate()

        elif player.find_touch('terminate2', monitor, tap=False):
            return terminate()

        elif player.find_touch('mission', monitor, tap=False):
            if player.find_touch('assist_1920x1080', monitor, tap=True):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    player.find_touch('setting_1920x1080', monitor, tap=True)
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    player.find_touch('mode_1920x1080', monitor, tap=True)
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break
            elif player.find_touch('assisting', monitor, tap=False):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    player.find_touch('setting_1920x1080', monitor, tap=True)
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    player.find_touch('mode_1920x1080', monitor, tap=True)
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break
            elif player.find_touch('assisting_1', monitor, tap=False):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    player.find_touch('setting_1920x1080', monitor, tap=True)
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    player.find_touch('mode_1920x1080', monitor, tap=True)
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break
            elif player.find_touch('assisting_2', monitor, tap=False):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    player.find_touch('setting_1920x1080', monitor, tap=True)
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    player.find_touch('mode_1920x1080', monitor, tap=True)
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break
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

'''
1920x1080
缺 w_1
response
'''
def terminate():
    while True:
        now_time = time.strftime("%Y-%m-%d", time.localtime())
        # print(now_time)
        now_time = Interval.between(now_time, now_time)
        want_time = Interval.between("2022-04-06", "2022-05-01")
        # print(want_time)
        if now_time not in want_time:
            quit()
        player.find_touch('w_1920x1080', monitor, tap=True)
        player.find_touch('w_1', monitor, tap=True)
        player.find_touch('w_2', monitor, tap=True)
        player.find_touch('start_1920x1080', monitor, tap=True)
        player.find_touch('start_game_1920x1080', monitor, tap=True)
        if player.find_touch('assist_1920x1080', monitor, tap=True):
            player.find_touch('setting_1920x1080', monitor, tap=True)
            if player.find_touch('mode_1920x1080', monitor, tap=True):
                return auto_play_w_multi()
        time.sleep(3)



def menu(debug=False):
    menu_list = [
        #[auto_play_w, '女兒工作囉 解析度:1360x765'],
        [auto_play_w_multi, '解析度:1920x1080']
    ]
    now_time = time.strftime("%Y-%m-%d", time.localtime())
    #print(now_time)
    now_time = Interval.between(now_time, now_time)
    want_time = Interval.between("2022-04-05", "2022-04-07")
    if now_time not in want_time:
        print("!!!! 時間到了 !!!!\n" + "\n喜歡的話可以再聯絡")
        quit()
    i = 0
    for func, des in menu_list:
        msg = str(i) + ": " + des + '\n'
        print(msg)
        i += 1
    #player.alarm(1)
    raw = input("選擇功能模式：")
    index = int(raw)
    func, des = menu_list[index]
    print('已選擇功能： ' + des + '\n')

    global n, m, s, h
    #n = int(input('輸入螢幕寬度: '))
    #h = int(input('輸入螢幕高度: '))
    upleft = (0, 0)
    downright = (1920, 1080)
    a, b = upleft
    c, d = downright
    global monitor
    monitor = {"top": b, "left": a, "width": c, "height": d}
    m = int(input(
                  '1.亞丁城\n' +
                  '2.說話之島\n' +
                  '3.黑戰艦\n' +
                  '4.古魯丁\n' +
                  '5.妖精森林\n' +
                  '6.螞蟻洞窟\n\n' +
                  '選擇掛機地點: '))
    while m < 1 or m > 6:
        print("\n!!!!!!!!重新輸入範圍內的數字!!!!!!!!\n")
        m = int(input(
            '1.亞丁城\n' +
            '2.說話之島\n' +
            '3.黑戰艦\n' +
            '4.古魯丁\n' +
            '5.妖精森林\n' +
            '6.螞蟻洞窟\n\n' +
            '選擇掛機地點: '))

    s = float(input('輸入第幾層: '))
    func()






if __name__ == '__main__':

    #while True:
        #pt = player.random_x(60)
     #   pt = win32api.GetCursorPos()
     #   print(pt)
    # pyinstaller -F autorun.py
    menu()
    # img = Image.open(r"wanted/blood.png")
    # print(pytesseract.image_to_string(img, lang="eng"))
