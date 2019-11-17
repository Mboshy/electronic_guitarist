import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(0)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)


def switcher():
    while 1:
        inkey = input("Give a number ->")
        inkey = int(inkey)
        print("oooo ", inkey == 1)

        if inkey == 1:
            GPIO.output(2, 1)
            time.sleep(2)
            GPIO.output(2, 0)
        if inkey == 2:
            GPIO.output(3, 1)
            time.sleep(2)
            GPIO.output(3, 0)
        if inkey == 3:
            GPIO.output(4, 1)
            time.sleep(2)
            GPIO.output(4, 0)
        if inkey == 4:
            GPIO.output(5, 1)
            time.sleep(2)
            GPIO.output(5, 0)
        if inkey == 5:
            GPIO.output(6, 1)
            time.sleep(2)
            GPIO.output(6, 0)
        if inkey == 6:
            GPIO.output(7, 1)
            time.sleep(2)
            GPIO.output(7, 0)
        if inkey == 7:
            GPIO.output(8, 1)
            time.sleep(2)
            GPIO.output(8, 0)
        if inkey == 8:
            GPIO.output(9, 1)
            time.sleep(2)
            GPIO.output(9, 0)
        if inkey == 9:
            GPIO.output(10, 1)
            time.sleep(2)
            GPIO.output(10, 0)
        if inkey == 10:
            GPIO.output(11, 1)
            time.sleep(2)
            GPIO.output(11, 0)
        if inkey == 11:
            GPIO.output(12, 1)
            time.sleep(2)
            GPIO.output(12, 0)
        if inkey == 12:
            GPIO.output(13, 1)
            time.sleep(2)
            GPIO.output(13, 0)
        if inkey == 13:
            GPIO.output(14, 1)
            time.sleep(2)
            GPIO.output(14, 0)
        if inkey == 14:
            GPIO.output(15, 1)
            time.sleep(2)
            GPIO.output(15, 0)
        if inkey == 15:
            GPIO.output(16, 1)
            time.sleep(2)
            GPIO.output(16, 0)
        if inkey == 16:
            GPIO.output(17, 1)
            time.sleep(2)
            GPIO.output(17, 0)
        if inkey == 17:
            GPIO.output(18, 1)
            time.sleep(2)
            GPIO.output(18, 0)
        if inkey == 18:
            GPIO.output(19, 1)
            time.sleep(2)
            GPIO.output(19, 0)
        if inkey == 19:
            GPIO.output(20, 1)
            time.sleep(2)
            GPIO.output(20, 0)
        if inkey == 20:
            GPIO.output(21, 1)
            time.sleep(2)
            GPIO.output(21, 0)
        if inkey == 21:
            GPIO.output(22, 1)
            time.sleep(2)
            GPIO.output(22, 0)
        if inkey == 22:
            GPIO.output(23, 1)
            time.sleep(2)
            GPIO.output(23, 0)
        if inkey == 23:
            GPIO.output(24, 1)
            time.sleep(2)
            GPIO.output(24, 0)
        if inkey == 24:
            GPIO.output(25, 1)
            time.sleep(2)
            GPIO.output(25, 0)
        if inkey == 25:
            GPIO.output(26, 1)
            time.sleep(2)
            GPIO.output(26, 0)
        if inkey == 26:
            GPIO.output(27, 1)
            time.sleep(2)
            GPIO.output(27, 0)
        if inkey == 0:
            break


def main():
    setup()
    switcher()


if __name__ == '__main__':
    main()
