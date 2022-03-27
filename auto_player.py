import cv2, numpy, time, os, random, threading
import pyautogui
from winsound import Beep
from PIL import ImageGrab
from settings import *

pyautogui.PAUSE = 0.01

def adb_test():
    if mode == 1:
        return
    raw_content = os.popen('adb devices').read()
    row_list = raw_content.split('List of devices attached\n')[1].split('\n')
    devices_list = [i for i in row_list if len(i) > 1]
    print(raw_content)
    devices_count = len(devices_list)
    assert devices_count > 0,   + devices_count



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


def screen_shot():
    if mode == 0:
        a = "adb shell screencap -p sdcard/screen.jpg"
        b = "adb pull sdcard/screen.jpg ./screen"
        for row in [a, b]:
            time.sleep(0.1)
            os.system(row)
    else:  # 桌面截屏
        screen = ImageGrab.grab()
        screen.save('./screen/screen.jpg')
    print('截圖已完成 ', time.ctime())
    screen = cv2.imread('./screen/screen.jpg')
    return screen

)
def touch(pos):
    x, y = pos
    if mode == 0:
        a = "adb shell input touchscreen tap {0} {1}".format(x, y)
        os.system(a)
    else:
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)



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


def locate(screen, wanted, show=0):
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



def random_offset(p, w=40, h=20):
    a, b = p
    w, h = int(w / 3), int(h / 3)
    c, d = random.randint(-w, w), random.randint(-h, h)
    e, f = a + c, b + d
    y = [e, f]
    return (y)


def random_delay(x=0.1, y=0.6):
    t = random.uniform(x, y)
    time.sleep(t)


def find_touch(target, tap=True):
    screen = screen_shot()
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
        return True
    else:
        print('N 未找到目標 ', target)
        return False




