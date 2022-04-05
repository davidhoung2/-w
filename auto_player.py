import cv2, numpy, time, os, random, threading
import mss
import pyautogui
from winsound import Beep

import win32api
import win32con
from PIL import ImageGrab
from interval import Interval

from settings import *

pyautogui.PAUSE = 0.01




# -------------------------------------------------------------------------------------------

def adb_test():
    if mode == 1:
        return
    raw_content = os.popen('adb devices').read()
    row_list = raw_content.split('List of devices attached\n')[1].split('\n')
    devices_list = [i for i in row_list if len(i) > 1]
    print(raw_content)
    devices_count = len(devices_list)
    assert devices_count > 0, + devices_count


def time_out(func):
    def wrap_func(*args, **kwargs):
        restart = lambda: func(*args, **kwargs)
        timer = threading.Timer(3, restart)
        timer.start()
        func(*args, **kwargs)
        timer.cancel()

    return wrap_func


def retry(func):
    def wrap_func(*args, **kwargs):
        try:
            re = func(*args, **kwargs)
        except:
            print("匹配錯誤")
            time.sleep(3)
            re = func(*args, **kwargs)
        return re

    return wrap_func


def screen_shot(monitor):
    if mode == 0:
        a = "adb shell screencap -p sdcard/screen.jpg"
        b = "adb pull sdcard/screen.jpg ./screen"
        for row in [a, b]:
            time.sleep(0.1)
            os.system(row)
    else:  # 桌面截屏
        print(time.ctime())
        im = numpy.array(mss.mss().grab(monitor))
        screen = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
    return screen


def touch(pos):
    x, y = pos
    print(pos)

    pt = win32api.GetCursorPos()
    pt_x = pt[0]
    pt_y = pt[1]

    win32api.mouse_event(0x0001, x - pt_x, y - pt_y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x - pt_x, y - pt_y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x - pt_x, y - pt_y, 0, 0)

'''
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
'''
'''
    ghub.mouse_xy((x - pt_x), (y - pt_y))
    ghub.mouse_down(1)
    ghub.mouse_up(1)


'''
def touch_p(pos, offset):
    x, y = pos
    print(pos)
    pt = win32api.GetCursorPos()

    pt_x = pt[0]
    pt_y = pt[1] - offset
    win32api.mouse_event(0x0001, int(x - pt_x), int(y - pt_y), 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(x - pt_x), int(y - pt_y), 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int(x - pt_x), int(y - pt_y), 0, 0)


def alarm(n=3):
    frequency = 1500
    last = 500
    for n in range(n):
        Beep(frequency, last)
        time.sleep(0.05)


def load_imgs():
    imgs = {}
    treshold = accuracy
    path = wanted_path
    file_list = os.listdir(path)

    for file in file_list:
        name = file.split('.')[0]
        file_path = path + '/' + file
        a = [cv2.imread(file_path), treshold, name]
        imgs[name] = a

    return imgs


imgs = load_imgs()


def locate(screen, wanted, show=bool(0)):
    loc_pos = []
    wanted, treshold, c_name = wanted
    result = cv2.matchTemplate(screen, wanted, cv2.TM_CCOEFF_NORMED)
    location = numpy.where(result >= treshold)

    h, w = wanted.shape[:-1]

    n, ex, ey = 1, 0, 0
    for pt in zip(*location[::-1]):
        x, y = pt[0] + int(w / 2), pt[1] + int(h / 2)
        if (x - ex) + (y - ey) < 15:
            continue
        ex, ey = x, y

        cv2.circle(screen, (x, y), 10, (0, 0, 255), 3)

        x, y = int(x), int(y)
        loc_pos.append([x, y])

    if show:
        cv2.imshow('we get', screen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return loc_pos


def cut(screen, upleft, downright):
    a, b = upleft
    c, d = downright
    screen = screen[b:d, a:c]
    return screen


def random_offset(p, w, h):
    a, b = p
    w, h = int(w / 3), int(h / 3)
    c, d = random.randint(-w, w), random.randint(-h, h)
    e, f = a + c, b + d
    y = [e, f]
    return y


def left_offset(p):
    a, b = p
    e, f = a - 100, b + 100
    y = [e, f]
    return y


def random_delay(x=2, y=2.5):
    t = random.uniform(x, y)
    time.sleep(t)


def find_touch_multi(target, monitor, dist, n, tap=True):
    screen = screen_shot(monitor)
    wanted = imgs[target]
    size = wanted[0].shape
    h, w, ___ = size
    pts = locate(screen, wanted)
    if pts:
        print('Y 已找到目標', target)
        xx = pts[0]
        xx = random_offset(xx, w, h)
        if tap:
            if dist < (n / 2):
                print('左邊')
                if xx[0] < (n / 2):
                    touch(xx)
                    random_delay()

            elif dist > (n / 2):
                print('右邊')
                if xx[0] > (n / 2):
                    touch(xx)
                    random_delay()
        return True
    else:
        print('N 未找到目標 ', target)
        return False


def find_touch(target, monitor, tap=True):
    screen = screen_shot(monitor)
    wanted = imgs[target]
    size = wanted[0].shape
    h, w, ___ = size
    pts = locate(screen, wanted)
    if pts:
        print('Y 已找到目標', target)
        xx = pts[0]
        xx = random_offset(xx, w, h)
        if tap:
            touch(xx)
            random_delay()
        return xx
    else:
        print('N 未找到目標 ', target)
        return False


def find_touch_unrand(target, monitor, tap=True):
    screen = screen_shot(monitor)
    wanted = imgs[target]
    pts = locate(screen, wanted)
    if pts:
        print('Y 已找到目標', target)
        xx = pts[0]
        if tap:
            touch(xx)
            random_delay()
        return xx
    else:
        print('N 未找到目標 ', target)
        return False


def find_touch_moveleft(target, monitor, tap=True):
    screen = screen_shot(monitor)
    wanted = imgs[target]
    pts = locate(screen, wanted)
    if pts:
        print('Y 已找到目標', target)
        xx = pts[0]
        xx = left_offset(xx)
        if tap:
            touch(xx)
            random_delay()
        return xx
    else:
        print('N 未找到目標 ', target)
        return False


# 判斷時間
def time_todo():
    now_time = time.strftime("%H:%M:%S", time.localtime())
    now_time = Interval.between(now_time, now_time)
    want_time = Interval.between("13:00:00", "17:00:00")
    if now_time in want_time:
        print("Yes")
    else:
        print("NO")
    time.sleep(2)

def time_crash():
    now_time = time.strftime("%H:%M:%S", time.localtime())
    now_time = Interval.between(now_time, now_time)
    want_time = Interval.between("13:00:00", "17:00:00")
    if now_time in want_time:
        print("Yes")
    else:
        print("NO")
    time.sleep(2)
'''
    只偵測血瓶那一塊區域(修改monitor的範圍)
    if 找到0時:   
        if 同時找到1~9 的話:
            break
        else:
            做後續回程買藥的動作
        
'''
