import goprolib.HERO4.HERO4 as HERO4
import datetime
import time


def main(path='/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_13 GoPro Auto'):
    h4 = HERO4.HERO4()
    h4.download_all(delete_after_download=True, path=path)

if __name__ == '__main__':
    while True:
        try:
            main('/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15_GoPro Tests')
        except:
            print(datetime.datetime.now())
        time.sleep(5)
