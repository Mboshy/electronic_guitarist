import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import glob

from notes import Note, Staff
from dictio import pitch_dict


def image_choice():
    """
    Choosing photo with music notation to be played.

    :return: Photo with music notation
    """
    songs = {}
    chosen = False
    index = 1

    for file in glob.glob('samples/songs/*'):
        f = file.split("songs\\", 1)[1]
        print('{}.'.format(index), f.split(".", 1)[0])
        songs[f.split(".", 1)[0]] = f
        index += 1

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


def image_preprocessing(image):
    """
    Required processes on the image is made to better representation of key points.

    :param image: Chosen photo to read
    :return: Processed image
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded = cv2.Canny(gray, 50, 200)
    return thresholded


def lines_detection(imag, scale):
    """
    It detects all horizontal lines with specified parameters.

    :param imag: Image which contains music staff
    :param scale: Scale of approximation
    :return: List of staffs' coordinates
    """
    image = image_preprocessing(imag)

    # Detect all vertical lines
    lines = cv2.HoughLinesP(image, 1, np.pi/180, 490, minLineLength=150, maxLineGap=150)
    lines = sorted(lines, key=lambda x: x[0][1])

    # Selection of detected lines
    coordinates = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        coordinates.append(int(y1))
        try:
            if abs(coordinates[-2] - y1) < 4*scale:
                coordinates[-2] = int((coordinates[-2] + y1) / 2)
                del coordinates[-1]
        except Exception as e:
            pass

    return coordinates


def crop(image):
    """
    It crops whole image for smaller parts containing only one staff

    :param image: Image containing music notation
    :return: Cropped image with staff
    """
    coor = lines_detection(image, 1)

    # Cropping image
    cropped = []
    for i in range(int(len(coor) / 5)):
        space = abs(coor[i*5 + 1] - coor[i*5])
        crop_img = image[coor[i*5] - 3*space: coor[i*5 + 4] + 5*space, 0:image.shape[1]]
        cropped.append(crop_img)
    return cropped


def pitch_define(y_pos, coordinates):
    """
    It defines the pitch of notes (it is limited to only basic notes for guitar)

    :param y_pos: Y coordinates of note
    :param coordinates: List of coordinates of staff
    :return: Name with string of detected note
    """
    staff = Staff(coordinates)
    if staff.line_bottom_3 - y_pos < 0:
        return 'E6'
    elif abs(staff.line_bottom_3 - y_pos) < ceil(staff.space_between * 1/3.0):
        return 'F6'
    elif abs(staff.line_bottom_2 - y_pos) < ceil(staff.space_between * 1/3.0):
        return 'A5'
    elif staff.line_bottom_3 > y_pos > staff.line_bottom_2:
        return 'G6'
    elif abs(staff.line_bottom_1 - y_pos) < ceil(staff.space_between * 1/3.0):
        return 'C5'
    elif staff.line_bottom_2 > y_pos > staff.line_bottom_1:
        return 'B5'
    elif abs(staff.line_1 - y_pos) < ceil(staff.space_between * 1/3.0):
        return 'E4'
    elif staff.line_bottom_1 > y_pos > staff.line_1:
        return 'D4'
    elif abs(staff.line_2 - y_pos) < ceil(staff.space_between * 1 / 3.0):
        return 'G3'
    elif staff.line_1 > y_pos > staff.line_2:
        return 'F4'
    elif abs(staff.line_3 - y_pos) < ceil(staff.space_between * 1 / 3.0):
        return 'B2'
    elif staff.line_2 > y_pos > staff.line_3:
        return 'A3'
    elif abs(staff.line_4 - y_pos) < ceil(staff.space_between * 1 / 3.0):
        return 'D2'
    elif staff.line_3 > y_pos > staff.line_4:
        return 'C2'
    elif abs(staff.line_5 - y_pos) < ceil(staff.space_between * 1 / 3.0):
        return 'F1'
    elif staff.line_4 > y_pos > staff.line_5:
        return 'E1'
    elif staff.line_5 > y_pos > staff.line_top:
        return 'G1'
    else:
        return 'UPS'


def note_detection(image, templates):
    """
    It takes whole picture and detect each staff and all notes

    :param image: Image with music notation
    :param templates: Images with templates
    :return: List of objects of class Note
    """
    ind = 0
    notes = []
    repeat = False
    scale = 1

    for im in crop(image):
        extent = im.shape[1]/800.
        notes_aux = []
        coordinates = lines_detection(im, scale)
        imag = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        for temp in templates:
            if 'half' in temp:
                length = 1./2
            else:
                length = 1./4
            template = cv2.imread(temp, 0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(imag, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            loc = np.asarray(loc)
            c = list(zip(loc[1], loc[0]))
            c = sorted(c, key=lambda x: x[0])

            for pt in c:
                pitch = pitch_define(int(pt[1] + h/2), coordinates)
                note = Note(pitch_dict[pitch], ind, length, pt[0], pt[1])
                for n in notes_aux:
                    if abs(pt[0] - n.x) < 6*extent:
                        repeat = True
                        break
                if not repeat:
                    notes_aux.append(note)
                    ind += 1
                repeat = False

        notes_aux = sorted(notes_aux, key=lambda no: no.x)
        notes += notes_aux
        for pt in notes_aux:
            cv2.rectangle(im, (pt.x, pt.y), (pt.x + w, pt.y + h), (0, 0, 255), 1)
        plt.imshow(im)
        plt.show()

    return notes


def note_recognition(image, templates):
    """
    It creates most important data for Raspberry Pi to control actuators

    :param image: Image with music notation
    :param templates: Images with templates
    :return: 3 lists of: pitch of tone, strings of tone, length of tone
    """
    notes = note_detection(image, templates)
    pitch = [n.pitch for n in notes]
    strings = [n.string for n in notes]
    lenght = [n.lenght for n in notes]

    return pitch, strings, lenght
