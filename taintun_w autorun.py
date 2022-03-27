import time, os
import auto_player as player


def get_pictures():
    player.screen_shot()


def auto_play_w():
    tele_pos = [1846, 994]
    setting_pos = [33, 858]
    mode_pos = [956, 565]
    while True:
        if player.find_touch('fight', tap=False):
            xx = player.random_offset(tele_pos, 2, 2)
            player.touch(xx)
            player.random_delay()
            time.sleep(1)
            xx = player.random_offset(setting_pos, 1, 1)
            player.touch(xx)
            player.random_delay()
            xx = player.random_offset(mode_pos, 20, 20)
            player.touch(xx)
            player.random_delay()
            #player.find_touch('setting', tap=True)
            #player.find_touch('mode', tap=True)
        else:
            print("no")
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
    menu()
