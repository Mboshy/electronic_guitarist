# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from math import ceil
#
# from notes import Note, Staff
# from dictio import pitch_dict
#
# img = cv2.imread('samples/moonlight.png', cv2.IMREAD_COLOR)
#
#
# def image_preprocessing(img):
#     bitwise = cv2.bitwise_or(img, img)
#     gray = cv2.cvtColor(bitwise, cv2.COLOR_BGR2GRAY)
#     thresholded = cv2.Canny(gray, 50, 200)
#     return thresholded
#
#
# def lines_detection(picture, scale):
#     image = image_preprocessing(picture)
#     # Detect lines
#     lines = cv2.HoughLinesP(image, 1, np.pi/180, 490, minLineLength=150, maxLineGap=150)
#     lines = sorted(lines, key=lambda x: x[0][1])
#     coordinates = []
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         # cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
#         coordinates.append(int(y1))
#         try:
#             if abs(coordinates[-2] - y1) < 4*scale:
#                 coordinates[-2] = int((coordinates[-2] + y1) / 2)
#                 del coordinates[-1]
#         except Exception as e:
#             print(str(e))
#     print(len(coordinates))
#     return coordinates
#
#
# def crop():
#     coor = lines_detection(img, 1)
#     cropped = []
#     for i in range(int(len(coor) / 5)):
#         space = abs(coor[i*5 + 1] - coor[i*5])
#         crop_img = img[coor[i*5] - 3*space: coor[i*5 + 4] + 5*space, 0:img.shape[1]]
#         cropped.append(crop_img)
#     return cropped
#
#
# def pitch_define(y_pos, coordinates):
#     staff = Staff(coordinates)
#     if staff.line_bottom_3 - y_pos < 0:
#         return 'E6'
#     elif abs(staff.line_bottom_3 - y_pos) < ceil(staff.space_between * 1/4.0):
#         return 'F6'
#     elif abs(staff.line_bottom_2 - y_pos) < ceil(staff.space_between * 1/4.0):
#         return 'A5'
#     elif staff.line_bottom_3 > y_pos > staff.line_bottom_2:
#         return 'G6'
#     elif abs(staff.line_bottom_1 - y_pos) < ceil(staff.space_between * 1/4.0):
#         return 'C5'
#     elif staff.line_bottom_2 > y_pos > staff.line_bottom_1:
#         return 'B5'
#     elif abs(staff.line_1 - y_pos) < ceil(staff.space_between * 1/4.0):
#         return 'E4'
#     elif staff.line_bottom_1 > y_pos > staff.line_1:
#         return 'D4'
#     elif abs(staff.line_2 - y_pos) < ceil(staff.space_between * 1 / 4.0):
#         return 'G3'
#     elif staff.line_1 > y_pos > staff.line_2:
#         return 'F4'
#     elif abs(staff.line_3 - y_pos) < ceil(staff.space_between * 1 / 4.0):
#         return 'B2'
#     elif staff.line_2 > y_pos > staff.line_3:
#         return 'A3'
#     elif abs(staff.line_4 - y_pos) < ceil(staff.space_between * 1 / 4.0):
#         return 'D2'
#     elif staff.line_3 > y_pos > staff.line_4:
#         return 'C2'
#     elif abs(staff.line_5 - y_pos) < ceil(staff.space_between * 1 / 4.0):
#         return 'F1'
#     elif staff.line_4 > y_pos > staff.line_5:
#         return 'E1'
#     # elif abs(staff.line_top - y_pos) < ceil(staff.space_between * 1 / 4.0):
#     #     return 'A1'
#     elif staff.line_5 > y_pos > staff.line_top:
#         return 'G1'
#     else:
#         return 'UPS'
#
#
# def blob_params():
#     params = cv2.SimpleBlobDetector_Params()
#     params.minThreshold = 0
#     params.maxThreshold = 200
#     params.minArea = 100
#     params.filterByInertia = 1
#     params.minInertiaRatio = 0.3
#     params.maxInertiaRatio = 0.5
#     return params
#
#
# def blob_notes_position():
#     notes = []
#     ind = 0
#     scale = 2
#     for im in crop():
#         im = cv2.resize(im, (int(scale * im.shape[1]), int(scale * im.shape[0])))
#         coordinates = lines_detection(im, scale)
#         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#         detector = cv2.SimpleBlobDetector_create(blob_params())
#         keypoints = detector.detect(gray)
#         keypoints = sorted(keypoints, key=lambda x: x.pt[0])
#         # drawing cross on every detected note
#         for keyp in keypoints:
#             processed_image = cv2.drawMarker(im, (int(keyp.pt[0]), int(keyp.pt[1])), (255, 0, 0),
#                                          markerType=cv2.MARKER_SQUARE, markerSize=30, thickness=2)
#             pitch = pitch_define(int(keyp.pt[1]), coordinates)
#             note = Note(pitch_dict[pitch], ind, 1/4, 0)
#             notes.append(note)
#             ind += 1
#
#         print(len(notes))
#         plt.imshow(processed_image)
#         plt.show()
#
#     return notes
#
#
# def note_recognition():
#     notes = blob_notes_position()
#     pitch = [n.pitch for n in notes]
#     strings = [n.string for n in notes]
#     lenght = [n.lenght for n in notes]
#
#     return pitch, strings, lenght
#
#
# def main():
#     note_recognition()
#
#
# if __name__ == '__main__':
#     main()

import glob
import cv2


def image_choice():
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
    # print(songs[choice])

    return image


def templates():
    list_template = []

    for file in glob.glob('samples/notes/quarter/*'):
        list_template.append(file)
    for file in glob.glob('samples/notes/half/*'):
        list_template.append(file)

    return list_template

if __name__ == '__main__':
    # image_choice()
    templates()
