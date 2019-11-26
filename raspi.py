import RPi.GPIO as GPIO
import time
from note_recognition import note_recognition
from dictio import fret_dict, string_dict, hit_dict
import cv2
import glob


def image_choice():
    """
    Choosing photo with music notation to be played.

    :return: Photo with music notation
    """
    songs = {}
    chosen = False
    index = 1

    # Getting each song from directory
    for file in glob.glob('samples/songs/*'):
        f = file.split("songs\\", 1)[1]
        print('{}.'.format(index), f.split(".", 1)[0])
        songs[f.split(".", 1)[0]] = f
        index += 1

    # Loop with latch to choose an image
    while not chosen:
        choice = input("Choose one song from above: ")
        if choice in songs.keys():
            chosen = True

    image = cv2.imread('samples/songs/' + songs[choice], cv2.IMREAD_COLOR)

    return image


def template_list():
    """
    Getting all the pictures with templates note

    :return: list of templates
    """
    list_template = []

    for file in glob.glob('samples/notes/quarter/*'):
        list_template.append(file)
    for file in glob.glob('samples/notes/half/*'):
        list_template.append(file)

    return list_template


def setup():
    """
    It sets all GPIO for output mode
    """
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


def switcher(image, templates, tempo):
    """
    It control all GPIO and switch the state of voltage.

    :param image: Image with music notation
    :param templates: Images with templates
    """
    pitch, string, length = note_recognition(image, templates)

    for p, s, l in zip(pitch, string, length):
        try:
            time.sleep(0.1)
            GPIO.output(fret_dict[p], 1)
            time.sleep(0.1)
        except Exception as e:
            pass

        try:
            hit_dict[s] = not hit_dict[s]
            GPIO.output(string_dict[s], hit_dict[s])
            time.sleep(tempo * l)
        except Exception as e:
            pass

        try:
            time.sleep(0.1)
            GPIO.output(fret_dict[p], 0)
            time.sleep(0.1)
        except Exception as e:
            pass


def switchi(image, templates, tempo):
    """
    Auxiliary function printing information of each note.

    :param image: Image with music notation
    :param templates: Images with templates    """
    pitch, string, length = note_recognition(image, templates)

    for p, s, l in zip(pitch, string, length):
        try:
            hit_dict[s] = not hit_dict[s]
            print('Fret:', p % 10, '  String:', s, ' 5V:', hit_dict[s], ' Length:', tempo * l / 5)
        except Exception as e:
            pass


def main():
    tempo = 1.0
    image = image_choice()
    templates = template_list()

    setup()
    switcher(image, templates, tempo)
    switchi(image, templates, tempo)

    # Setting all actuators to idle position
    for i in range(2, 27):
        GPIO.output(i, 0)
    GPIO.cleanup()


if __name__ == '__main__':
    main()
