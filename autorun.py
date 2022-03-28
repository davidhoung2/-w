import time, os

import win32api

import auto_player as player


def get_pictures():
    player.screen_shot()


def auto_play_w():
    tele_pos = [1804, 715]
    setting_pos = [551, 511]
    mode_pos = [1196, 433]
    while True:
        if player.find_touch('fight', tap=False):
            player.random_delay()
            xx = player.random_offset(tele_pos, 5, 5)
            player.touch(xx)
            player.random_delay()
            xx = player.random_offset(setting_pos, 1, 1)
            player.touch(xx)
            player.random_delay()
            xx = player.random_offset(mode_pos, 20, 20)
            player.touch(xx)
            player.random_delay()
        time.sleep(1)


def menu(debug=False):
    menu_list = [
        [get_pictures, '屏幕截圖'],
        [auto_play_w, '自動烙幹'],
    ]

    while True:
        i = 0
        for func, des in menu_list:
            msg = str(i) + ": " + des + '\n'
            print(msg)
            i += 1
        player.alarm(1)
        raw = input("選擇功能模式：") if not debug else 1
        index = int(raw) if raw else 1
        func, des = menu_list[index]
        print('已選擇功能： ' + des)
        func()


if __name__ == '__main__':
    '''while True:
        pt = win32api.GetCursorPos()
        print(pt)'''
    menu()
