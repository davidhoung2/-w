import datetime
import random
import time

from interval import Interval
import numpy as np
import pyautogui
from PIL import Image
import cv2
import mss
import win32api
import win32con
import auto_player as player

def prison_move(area , floor):
    select_move = 113
    if player.find_touch('lookup', monitor, tap=True) or player.find_touch('lookup1', monitor, tap=True):
        if player.find_touch('prison', monitor, tap=True):
            if area == 1:
                while not player.find_touch('prison_1', monitor, tap=True):
                    if player.find_touch('prison_1', monitor, tap=True):
                        break
                if floor == 1:
                    player.find_touch_unrand('move_prison', monitor, tap=True)
                    while not player.find_touch('correct', monitor, tap=True):
                        if player.find_touch('correct', monitor, tap=True):
                            break
                if floor == 2:
                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
                if floor == 3:
                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
            if area == 2:
                while not player.find_touch('prison_2', monitor, tap=True):
                    if player.find_touch('prison_2', monitor, tap=True):
                        break
                if floor == 1:
                    player.find_touch('move_prison', monitor, tap=True)
                    while not player.find_touch('correct', monitor, tap=True):
                        if player.find_touch('correct', monitor, tap=True):
                            break
                if floor == 2:
                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
            if area == 3:
                while not player.find_touch('prison_3', monitor, tap=True):
                    if player.find_touch('prison_3', monitor, tap=True):
                        break
                if floor == 1:
                    player.find_touch_unrand('move_prison', monitor, tap=True)
                    while not player.find_touch('correct', monitor, tap=True):
                        if player.find_touch('correct', monitor, tap=True):
                            break
                if floor == 2:
                    if player.find_touch('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
                if floor == 3:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
            if area == 4:
                while not player.find_touch('prison_4', monitor, tap=True):
                    if player.find_touch('prison_4', monitor, tap=True):
                        break
                if floor == 1:
                    player.find_touch_unrand('move_prison', monitor, tap=True)
                    while not player.find_touch('correct', monitor, tap=True):
                        if player.find_touch('correct', monitor, tap=True):
                            break
                if floor == 2:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
                if floor == 3:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
                # 重第三層走入

                '''
                傳送到古魯丁3層

                1.點小地圖
                2.點到要的座標
                3.按住D 2秒
                4.偵測門
                if 偵測不到門:
                    repeat 1~4 
                '''
                if floor == 4:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 2)
                        player.touch_p(go, y)  # 傳到第三層
                        time.sleep(1)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
                        time.sleep(2)
                        if player.find_touch('assisting', monitor, tap=True) or player.find_touch('assisting_2',
                                                                                                  monitor, tap=True):
                            player.find_touch('assist', monitor, tap=True)

                        player.find_touch_moveleft('home_map1', monitor, tap=True)
                        time.sleep(2)
                        # 移動到位置
                        player.find_touch('flag_4', monitor, tap=True)
                        player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                        time.sleep(60)
                        win32api.keybd_event(68, 0, 0, 0)
                        time.sleep(3)
                        win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                        for i in range(5):
                            if player.find_touch('transport_door_44', monitor, tap=True):
                                break
                            else:
                                player.find_touch_moveleft('home_map1', monitor, tap=True)
                                time.sleep(2)
                                player.find_touch('flag_4', monitor, tap=True)
                                player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                                time.sleep(10)
                                win32api.keybd_event(68, 0, 0, 0)
                                time.sleep(2)
                                win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                if floor == 5:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 3)
                        player.touch_p(go, y)  # 傳到第三層
                        time.sleep(1)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
                        time.sleep(2)
                        if player.find_touch('assisting', monitor, tap=True) or player.find_touch('assisting_2',
                                                                                                  monitor, tap=True):
                            player.find_touch('assist', monitor, tap=True)

                        player.find_touch_moveleft('home_map1', monitor, tap=True)
                        time.sleep(2)
                        # 移動到位置
                        while not player.find_touch('flag_4', monitor, tap=True):
                            if player.find_touch('flag_4', monitor, tap=True):
                                break

                        player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                        time.sleep(60)
                        win32api.keybd_event(68, 0, 0, 0)
                        time.sleep(3)
                        win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                        for i in range(5):
                            if player.find_touch('transport_door_44', monitor, tap=True):
                                break
                            else:
                                player.find_touch_moveleft('home_map1', monitor, tap=True)
                                time.sleep(2)
                                player.find_touch('flag_4', monitor, tap=True)
                                player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                                time.sleep(10)
                                win32api.keybd_event(68, 0, 0, 0)
                                time.sleep(2)
                                win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                        #-------第四層到第五層----------
                        if player.find_touch('assisting', monitor, tap=True) or player.find_touch('assisting_2',
                                                                                                  monitor, tap=True):
                            player.find_touch('assist', monitor, tap=True)

                        player.find_touch_moveleft('home_map1', monitor, tap=True)
                        time.sleep(2)
                        # 移動到位置
                        while not player.find_touch('flag_41', monitor, tap=True):
                            if player.find_touch('flag_41', monitor, tap=True):
                                break

                        player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                        time.sleep(38)
                        win32api.keybd_event(65, 0, 0, 0)
                        time.sleep(2)
                        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
                        for i in range(5):
                            if player.find_touch('transport_door_44', monitor, tap=True):
                                break
                            else:
                                player.find_touch_moveleft('home_map1', monitor, tap=True)
                                time.sleep(2)
                                player.find_touch('flag_4', monitor, tap=True)
                                player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                                time.sleep(10)
                                win32api.keybd_event(68, 0, 0, 0)
                                time.sleep(2)
                                win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)

            if area == 5:
                pt = win32api.GetCursorPos()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(pt[0]), 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                time.sleep(2)
                while not player.find_touch('prison_5', monitor, tap=True):
                    if player.find_touch('prison_5', monitor, tap=True):
                        break

                if floor == 1:
                    player.find_touch_unrand('move_prison', monitor, tap=True)
                    while not player.find_touch('correct', monitor, tap=True):
                        if player.find_touch('correct', monitor, tap=True):
                            break

                if floor == 2:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break

                if floor == 3:
                    ss = 2
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (ss - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break

                        time.sleep(2)
                        if player.find_touch('assisting', monitor, tap=True) or player.find_touch(
                                'assisting_2', monitor, tap=True):
                            player.find_touch('assist', monitor, tap=True)

                        while not player.find_touch('small_map_5', monitor, tap=True):
                            if player.find_touch('small_map_5', monitor, tap=True):
                                break
                        time.sleep(2)
                        # 移動到位置
                        while not player.find_touch('flag_5', monitor, tap=True):
                            if player.find_touch('flag_5', monitor, tap=True):
                                break

                        while not player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True):
                            if player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True):
                                break

                        time.sleep(70)
                        win32api.keybd_event(65, 0, 0, 0)
                        time.sleep(1)
                        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
                        win32api.keybd_event(87, 0, 0, 0)
                        time.sleep(1)
                        win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
                        for i in range(5):
                            if player.find_touch('transport_door_44', monitor, tap=True):
                                break
                            else:
                                player.find_touch('small_map_6', monitor, tap=True)
                                time.sleep(2)
                                # 移動到位置
                                player.find_touch('flag_5', monitor, tap=True)
                                player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                                time.sleep(40)
                                win32api.keybd_event(65, 0, 0, 0)
                                time.sleep(1)
                                win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
                                win32api.keybd_event(87, 0, 0, 0)
                                time.sleep(1)
                                win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)

            if area == 6:
                pt = win32api.GetCursorPos()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(pt[0]), 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int((pt[0] - 1920) * 3.5), 0, 0, 0)
                time.sleep(1)
                player.find_touch('prison_6', monitor, tap=True)

                if floor == 1:
                    player.find_touch_unrand('move_prison', monitor, tap=True)
                    while not player.find_touch('correct', monitor, tap=True):
                        if player.find_touch('correct', monitor, tap=True):
                            break

                if floor == 2:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break

                if floor == 1.3:
                    ss = 3
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (ss - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break
                if floor == 4:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break

                if floor == 5:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break

                if floor == 6:
                    if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                        go = player.find_touch_unrand('move_prison', monitor, tap=False)
                        y = select_move * (floor - 1)
                        player.touch_p(go, y)
                        while not player.find_touch('correct', monitor, tap=True):
                            if player.find_touch('correct', monitor, tap=True):
                                break

                if floor > 6 or floor == 3:
                    pt = [int(1920 / 2), int(910)]
                    win32api.SetCursorPos(pt)
                    time.sleep(1.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, int((pt[0] - 1080) * 4), 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, int((pt[0] - 1080) * 4), 0, 0)
                    time.sleep(2)
                    if floor == 21:
                        ss = 3
                        if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                            go = player.find_touch_unrand('move_prison', monitor, tap=False)
                            y = select_move * (ss - 1)
                            player.touch_p(go, y)
                            while not player.find_touch('correct', monitor, tap=True):
                                if player.find_touch('correct', monitor, tap=True):
                                    break

                    if floor == 22:
                        ss = 4
                        if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                            go = player.find_touch_unrand('move_prison', monitor, tap=False)
                            y = select_move * (ss - 1)
                            player.touch_p(go, y)
                            while not player.find_touch('correct', monitor, tap=True):
                                if player.find_touch('correct', monitor, tap=True):
                                    break

                    if floor == 23:
                        ss = 5
                        if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                            go = player.find_touch_unrand('move_prison', monitor, tap=False)
                            y = select_move * (ss - 1)
                            player.touch_p(go, y)
                            while not player.find_touch('correct', monitor, tap=True):
                                if player.find_touch('correct', monitor, tap=True):
                                    break

                    if floor == 3:
                        ss = 5
                        if player.find_touch_unrand('move_prison', monitor, tap=False):  # 找到箭頭
                            go = player.find_touch_unrand('move_prison', monitor, tap=False)
                            y = select_move * (ss - 1)
                            player.touch_p(go, y)  # 傳到第三層
                            time.sleep(1)
                            while not player.find_touch('correct', monitor, tap=True):
                                if player.find_touch('correct', monitor, tap=True):
                                    break
                            time.sleep(2)
                            if player.find_touch('assisting', monitor, tap=True) or player.find_touch(
                                    'assisting_2', monitor, tap=True):
                                player.find_touch('assist', monitor, tap=True)

                            player.find_touch('small_map_6', monitor, tap=True)
                            time.sleep(2)
                            # 移動到位置
                            while not player.find_touch('flag_6', monitor, tap=True):
                                if player.find_touch('flag_6', monitor, tap=True):
                                    break
                            player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
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
                                    while not player.find_touch('flag_6', monitor, tap=True):
                                        if player.find_touch('flag_6', monitor, tap=True):
                                            break
                                    player.find_touch('move_4', monitor, tap=True) or player.find_touch('move_5', monitor, tap=True)
                                    time.sleep(10)
                                    win32api.keybd_event(65, 0, 0, 0)
                                    time.sleep(2)
                                    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)

def auto_play_w_multi():
    flag = 0
    while True:
        if win32api.GetAsyncKeyState(0x23):
            break
        x = random.randint(1, 4)

        if player.find_touch('fight_1920x1080', monitor, tap=False):
            flag = flag + x
            print("王八蛋來了!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            while not player.find_touch('teleport', monitor, tap=True):
                if player.find_touch('teleport', monitor, tap=True):
                    break
            #隨機飛
            if flag % 2 == 0:
                prison_move(4, 4)
            else:
                prison_move(6, 23)
        



        # 如果偵測到沒有紅藥水
        #elif player.find_touch('zero', monitor, tap=False) or player.find_touch('zero_1', monitor, tap=False):
        elif float(player.PerOfBlood()) < 0.7:
            win32api.keybd_event(27, 0, 0, 0)
            win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(1)
            while not player.find_touch_moveleft('home_map1', monitor, tap=True):
                player.find_touch_moveleft('home_map1', monitor, tap=True)
                if player.find_touch_moveleft('home_map1', monitor, tap=False):
                    break
            time.sleep(2)
            player.find_touch('teritory', monitor, tap=True)\
                or player.find_touch('teritory_1', monitor, tap=True)
            player.find_touch('home', monitor, tap=True) \
                or player.find_touch('home_1', monitor, tap=True)
            player.find_touch_unrand('home1', monitor, tap=True) \
                or player.find_touch_unrand('home1_1', monitor, tap=True)
            player.find_touch('home_tp', monitor, tap=True) \
                or player.find_touch('home_tp_1', monitor, tap=True)
            player.find_touch('correct', monitor, tap=True)
            time.sleep(10)
            player.find_touch('attack', monitor, tap=True)
            player.find_touch('shop', monitor, tap=True)
            if player.find_touch('shop_move', monitor, tap=True):
                time.sleep(20)
            player.find_touch('buy', monitor, tap=True)
            player.find_touch('buy_all', monitor, tap=True)
            player.find_touch('exit', monitor, tap=True)
            prison_move(m, s)

        elif player.find_touch('lookup', monitor, tap=False) or player.find_touch('lookup1', monitor, tap=False):
            if player.find_touch_unrand('assist_1920x1080', monitor, tap=False):
                if not player.find_touch_unrand('assisting_2', monitor, tap=False) \
                        or not player.find_touch_unrand('assisting_1', monitor, tap=False):
                    player.find_touch_unrand('assist_1920x1080', monitor, tap=True)
                    while not player.find_touch('setting_1920x1080', monitor, tap=True):
                        if player.find_touch('setting_1920x1080', monitor, tap=True):
                            break
                    while not player.find_touch('mode_1920x1080', monitor, tap=True):
                        if player.find_touch('mode_1920x1080', monitor, tap=True):
                            break

            if player.find_touch_unrand('assist_2', monitor, tap=False):
                if not player.find_touch_unrand('assisting_2', monitor, tap=False) \
                        or not player.find_touch_unrand('assisting_1', monitor, tap=False):
                    player.find_touch_unrand('assist_2', monitor, tap=True)
                    while not player.find_touch('setting_1920x1080', monitor, tap=True):
                        if player.find_touch('setting_1920x1080', monitor, tap=True):
                            break
                    while not player.find_touch('mode_1920x1080', monitor, tap=True):
                        if player.find_touch('mode_1920x1080', monitor, tap=True):
                            break

            elif player.find_touch_unrand('assisting', monitor, tap=False):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break
            elif player.find_touch_unrand('assisting_1', monitor, tap=False):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break
            elif player.find_touch_unrand('assisting_2', monitor, tap=False):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break
            elif player.find_touch_unrand('assisting_3', monitor, tap=False):
                while not player.find_touch('setting_1920x1080', monitor, tap=True):
                    if player.find_touch('setting_1920x1080', monitor, tap=True):
                        break
                while not player.find_touch('mode_1920x1080', monitor, tap=True):
                    if player.find_touch('mode_1920x1080', monitor, tap=True):
                        break

        elif x == 3:
            if player.find_touch('x', monitor, tap=True):
                return terminate()

            elif player.find_touch('no_response', monitor, tap=True):
                return terminate()

            elif player.find_touch('terminate_1920x1080', monitor, tap=False):
                return terminate()

            elif player.find_touch('terminate1', monitor, tap=False):
                return terminate()

            elif player.find_touch('terminate2', monitor, tap=False):
                return terminate()


        '''
        #夢幻知島掛機
        
        now_time = time.strftime("%H:%M:%S", time.localtime())
        print(now_time)
        now_time = Interval.between(now_time, now_time)
        want_time = Interval.between("20:00:00", "21:00:00")
        #如果時間到了
        if now_time in want_time:
            win32api.keybd_event(27, 0, 0, 0)
            win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(1)
            if player.find_touch('lookup', monitor, tap=True) or player.find_touch('lookup1', monitor, tap=True):
                player.find_touch('prison', monitor, tap=True)
                進來之後有四種屬性選擇
                if 按下進入風夢島:
                    time.sleep(3)
                    while not player.find_touch('assist_1920x1080', monitor, tap=True):
                        if player.find_touch('assist_1920x1080', monitor, tap=True):
                            break
                    while not player.find_touch('setting_1920x1080', monitor, tap=True):
                        if player.find_touch('setting_1920x1080', monitor, tap=True):
                            break
                    while not player.find_touch('mode_1920x1080', monitor, tap=True):
                        if player.find_touch('mode_1920x1080', monitor, tap=True):
                            break
                
                elif 按下進入火夢島:
                    time.sleep(3)
                    while not player.find_touch('assist_1920x1080', monitor, tap=True):
                        if player.find_touch('assist_1920x1080', monitor, tap=True):
                            break
                    while not player.find_touch('setting_1920x1080', monitor, tap=True):
                        if player.find_touch('setting_1920x1080', monitor, tap=True):
                            break
                    while not player.find_touch('mode_1920x1080', monitor, tap=True):
                        if player.find_touch('mode_1920x1080', monitor, tap=True):
                            break
        #時間過了        
        else:
            
        '''

        t = random.uniform(1, 1.5)
        time.sleep(t)



def terminate():
    while True:
        now_time = time.strftime("%Y-%m-%d", time.localtime())
        # print(now_time)
        #now_time = Interval.between(now_time, now_time)
        #want_time = Interval.between("2022-04-06", "2022-05-01")
        # print(want_time)
        #if now_time not in want_time:
        #    quit()
        player.find_touch('w_1920x1080', monitor, tap=True)
        player.find_touch('w_1', monitor, tap=True)
        player.find_touch('w_2', monitor, tap=True)
        player.find_touch('start_1920x1080', monitor, tap=True)
        player.find_touch('start_game_1920x1080', monitor, tap=True)
        time.sleep(6)
        return auto_play_w_multi()




def menu(debug=False):
    menu_list = [
        #[auto_play_w, '女兒工作囉 解析度:1360x765'],
        [auto_play_w_multi, '解析度:1920x1080']
    ]
    #now_time = time.strftime("%Y-%m-%d", time.localtime())
    #print(now_time)
    #now_time = Interval.between(now_time, now_time)
    #want_time = Interval.between("2022-04-06", "2022-05-01")
    #if now_time not in want_time:
    #    print("!!!! 時間到了 !!!!\n" + "\n喜歡的話可以再聯絡")
    #    quit()
    i = 0
    for func, des in menu_list:
        msg = str(i) + ": " + des + '\n'
        print(msg)
        i += 1
    player.alarm(1)
    '''
    raw = input("選擇功能模式：")
    index = int(raw)
    func, des = menu_list[index]
    print('已選擇功能： ' + des + '\n')
'''
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
    print("開始偵測了 :)")

    func()



if __name__ == '__main__':
    #pyinstaller -F autorun.py
    #menu()
    #debug = 1
    #while debug:
    menu()
